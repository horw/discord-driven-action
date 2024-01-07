import discord
import os
import json
import sys
import requests
import datetime
import psutil
from discord.ext import tasks
from PIL import ImageGrab, Image, ImageDraw
import io

from configure.settings import Config
from utils import bcolors, google_reader
from programs import bots_path, Fly

os.system("cls")
version = '1.0'

start = 0
TIME = None
TIME_CHECKPOINT = None
MUTE_TIME = None
ON_OFF = True
MSG_PASS = False

RESTART_PROCESS = False
FNULL = open(os.devnull, 'w')

sku_dict = {}
sites = {}

token = "TOKEN"

bcolors.printgreen("Reading path...")
try:
    bots_path = json.load(open('path.json'))
except:
    json.dump(bots_path, open('path.json', 'w+'), indent=4)
    bcolors.printred('Your file contains incorrect symbols.')

bot = Fly(bots_path[Fly.name])
config = None

bcolors.printgreen("Reading config...")
try:
    data = json.load(open('config.json', 'rb'))
    config = Config(**data)
except Exception as e:
    json.dump(Config().model_dump(), open('config.json', 'w+'), indent=4)
    sys.exit(0)

google_reader(sites, config.sheet_url)

line = ''
for site in sites:
    line += f'  {site}: {",".join(sites[site]["kw"])}\n'

print(f"Keyword:\n{line}")

window = None


def screenshot():
    if config.webhook:
        try:
            buf = io.BytesIO()
            img = ImageGrab.grab()
            img.save(buf, format="PNG")
            buf.seek(0)
            requests.post(config.webhook, files={'media': ('screen.png', buf)}, timeout=5)
        except Exception as e:
            print(f'Screenshot Error {e}')


def connect_window_error(error_str):
    print(error_str)
    print('Connect Window Error')
    input()
    sys.exit(0)


##READ TASKS
try:
    bot.DATA = open(bot.tasks_path.replace('tasks.csv', 'taskscopy.csv'), 'rb').read()
    # DATA_CA = open(TASKS_PATH.replace('tasks.csv', 'taskscopyCA.csv'), 'rb').read()
except:
    input('Tasks error')
    sys.exit(0)


##PROCESS WORK
def kill_process():
    for proc in psutil.process_iter():
        try:
            if proc.name() == bot.proc_name:
                proc.kill()
        except Exception as e:
            continue


# def start_process():
#     while PROC_NAME not in [pr.name() for pr in psutil.process_iter()]:
#         subprocess.Popen(PATH, stdout=FNULL, stderr=subprocess.STDOUT)
#         time.sleep(10)


def restart_func():
    global window
    bot.restart()



def open_link(link, site_link, sizes, sku, msg):
    global TIME, TIME_CHECKPOINT, RESTART_PROCESS, NETWORK_USAGE, current_tasks_sites, window
    print('Open Function...')
    if not RESTART_PROCESS:
        bot.start(link, sku, sizes)

    if site_link not in current_tasks_sites:
        current_tasks_sites.append(site_link)

    if TIME == None:
        TIME = datetime.datetime.now()
        TIME_CHECKPOINT = TIME

    t = datetime.datetime.now().isoformat().replace('T', ' ')[:-7]
    print(f"{t} Open {link}")

    t_close = (TIME + datetime.timedelta(seconds=config.timer)).isoformat().replace('T', ' ')[:-7]
    print(f"{t} Tasks will close at: {t_close}")

    if config.webhook:
        t = datetime.datetime.now().isoformat().replace('T', ' ')[:-7]
        embed = {}
        embed['title'] = f"AIO Blue Start Task"
        embed['color'] = 8190976
        embed['fields'] = []
        embed['fields'].append({'name': 'Time', 'value': f'{t}'})
        embed['fields'].append({'name': 'Bot Name', 'value': f"{bot['name']}"})
        embed['fields'].append({'name': 'MONITOR', 'value': msg.channel.name})
        embed['footer'] = {
            'icon_url': 'https://cdn.discordapp.com/attachments/696345463099621478/752526723806920744/106481578_2024239424376214_1105798686871767184_o.png',
            'text': 'Blue Cup'}
        requests.post(config.webhook, json={'embeds': [embed]})

        image = io.BytesIO(requests.get('https://images.footlocker.com/pi/{0}/small/{0}.jpeg'.format(sku)).content)
        image = Image.open(image)
        draw = ImageDraw.Draw(image)
        draw.text((10, 50), sku, fill=(0, 0, 0))
        output = io.BytesIO()
        image.convert("RGB").save(output, "PNG")
        img_data = output.getvalue()
        output.close()

        requests.post(config.webhook, files={'file': ('1.png', img_data)})

    screenshot()


## TASKS FILTER
current_tasks_count = []
current_tasks_sites = []
mute_list = []


def sku_filter(site_link, sizes, sku, msg):
    global current_tasks_count, mute_list
    link = '{}product/~/{}.html'.format(site_link, sku)

    if mute_list:
        mute_format = "{}/{}".format(site_link.split('www.')[-1].replace('/', ''), sku)
        if mute_format in mute_list:
            print("Muted: ", mute_format)
            return

    real_sku = sku
    # do filter on link not just sku
    sku = link

    if sku in sku_dict.keys():
        if datetime.datetime.strptime(sku_dict[sku], "%Y-%m-%dT%H:%M:%S.%f") + datetime.timedelta(
                seconds=config.interval) <= datetime.datetime.now():
            sku_dict[sku] = datetime.datetime.now().isoformat()
            for i in range(config.multiple):
                if current_tasks_count.count(sku) < config.maximum:
                    current_tasks_count.append(sku)
                    open_link(link, site_link, sizes, real_sku, msg)
    else:
        sku_dict[sku] = datetime.datetime.now().isoformat()
        for i in range(config.multiple):
            if current_tasks_count.count(sku) < config.maximum:
                current_tasks_count.append(sku)
                open_link(link, site_link, sizes, real_sku, msg)


@tasks.loop(seconds=10)
async def restart_task():
    global TIME, TIME_CHECKPOINT, MUTE_TIME
    global current_tasks_count, current_tasks_sites, mute_list, RESTART_PROCESS

    if mute_list:
        if MUTE_TIME:
            if datetime.datetime.now() >= MUTE_TIME:
                mute_list = []
                MUTE_TIME = None
                print('Mute List was clear')

    if TIME and ON_OFF:
        if TIME + datetime.timedelta(
                seconds=config.timer) < datetime.datetime.now() or TIME_CHECKPOINT + datetime.timedelta(
                seconds=config.checkpoint_timer) < datetime.datetime.now():
            try:
                RESTART_PROCESS = True
                restart_func()
                TIME = None
                TIME_CHECKPOINT = None
                RESTART_PROCESS = False
                current_tasks_count = []
                current_tasks_sites = []
                try:
                    if config.webhook:
                        requests.post(config.webhook,
                                      json={'embeds': [{'title': 'BQT Stop Task Success', 'color': 14423100}]})
                except:
                    pass
            except Exception as e:
                print(e)
                try:
                    if config.webhook:
                        requests.post(config.webhook,
                                      json={'embeds': [{'title': 'BQT Stop Task Error', 'color': 14423100}]})
                except:
                    pass
                print('Restart error')
            screenshot()


def get_sku(link):
    return link.split('/')[-1].split('.html')[0].strip()


def get_kw_sizes(skw):
    skw = skw.split('SS:')
    skw = [i.strip(' ').lower() for i in skw]
    if len(skw) == 2:
        return skw[0], skw[1]
    if len(skw) == 1:
        return skw[0], None
    return None, None


def get_link_sizes(slink):
    slink = slink.replace('!open', '').strip(' ').split('SS:')
    slink = [i.strip(' ') for i in slink]
    if len(slink) == 2:
        return slink[0], slink[1]
    if len(slink) == 1:
        return slink[0], None
    return None, None


def discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)
    # client = discord.Client(intents=intents, proxy="http://localhost:1080")

    ##START ROUTINE
    @client.event
    async def on_connect():
        global start
        if start == 0:
            bcolors.printgreen("Started, wait for restock...")
            start = 1
            restart_task.start()

    ##BOT MONITOR
    @client.event
    async def on_message(msg):

        global TIME, TIME_CHECKPOINT, MUTE_TIME
        global ON_OFF, MSG_PASS
        global current_tasks_count, current_tasks_sites, RESTART_PROCESS

        try:
            if msg.channel.id in config.channels_id and not MSG_PASS:
                if msg.embeds:
                    for embed in msg.embeds:
                        embed = embed.to_dict()
                        t = datetime.datetime.now().isoformat().replace('T', ' ')[:-7]
                        print(f'{t} Monitor {embed["title"]}')
                        for site in sites:
                            site_link = sites[site]['link']
                            if embed['url'].startswith(site_link):
                                for kw in sites[site]['kw']:
                                    sku = get_sku(embed['url'])
                                    kw, sizes = get_kw_sizes(kw)

                                    if kw == sku.lower():
                                        print('Found a suitable SKU')
                                        if TIME != None:
                                            TIME_CHECKPOINT = datetime.datetime.now()
                                            print(f'TIME CHECKPOINT {TIME_CHECKPOINT}')
                                        sku_filter(site_link, sizes, sku, msg)

            if msg.channel.id == 747763023300788287:
                if msg.content.startswith('!real_open'):
                    if msg.author.id == config.author_id:
                        real_open_url = msg.content.replace('!real_open', '').strip(' ')
                        for site in sites:
                            site_link = sites[site]['link']
                            if real_open_url.startswith(site_link):
                                for kw in sites[site]['kw']:
                                    sku = get_sku(real_open_url)
                                    kw, sizes = get_kw_sizes(kw)
                                    if kw == sku.lower():
                                        print('Found a suitable SKU')
                                        sku_filter(site_link, sizes, sku, msg)

            if msg.channel.id == 747763023300788287:
                if msg.author.id == config.author_id:
                    if msg.content.startswith('!open'):
                        try:
                            link, sizes = get_link_sizes(msg.content)
                            print(link, sizes)
                            sku = get_sku(link)
                            for site in sites:
                                site_link = sites[site]['link']
                                if link.startswith(site_link):
                                    open_link(link, site_link, sizes, sku, msg)
                                    return

                        except Exception as e:
                            print(e)
                            print('Open error')

                    if msg.content.startswith('!stop'):

                        if TIME and ON_OFF:
                            try:
                                RESTART_PROCESS = True
                                restart_func()
                                TIME = None
                                TIME_CHECKPOINT = None
                                RESTART_PROCESS = False
                                current_tasks_count = []
                                current_tasks_sites = []
                                try:
                                    if config.webhook:
                                        requests.post(config.webhook, json={
                                            'embeds': [{'title': 'BQT Stop Task Success', 'color': 14423100}]})
                                except:
                                    pass
                            except Exception as e:
                                print(e)
                                try:
                                    if config.webhook:
                                        requests.post(config.webhook, json={
                                            'embeds': [{'title': 'BQT Stop Task Error', 'color': 14423100}]})
                                except:
                                    pass
                                print('Stop error')
                            screenshot()

                    if msg.content.startswith('!N'):
                        ON_OFF = not ON_OFF
                        print(f'Restart: {ON_OFF}')

                    if msg.content.startswith('!P'):
                        MSG_PASS = not MSG_PASS
                        print(f'Pass Message: {MSG_PASS}')

                    if msg.content == 'update':
                        if config.sheet_url:
                            google_reader(sites, config.sheet_url)
                            line = ''
                            for site in sites:
                                line += f'  {site}: {",".join(sites[site]["kw"])}\n'
                            print(f"Keyword:\n{line}")
                        else:
                            print('You didnt set up sheet')

                    if msg.content.startswith('!M'):
                        command_ = msg.content.replace('!M', '').strip().replace('  ', ' ').split(' ')
                        template = ['eastbay.com', 'footaction.com', 'champssports.com', 'footlocker.com',
                                    'kidsfootlocker.com']
                        print(command_)
                        if len(command_) == 3 or len(command_) == 4:
                            mute_time, mute_site, mute_sku, *_other = command_
                            if _other:
                                if bot.name.lower() not in _other:
                                    print(f'Command for another bot {_other}')
                                    return
                            if mute_site.strip() != 'us':
                                template = [mute_site.strip()]
                            for mute_site in template:
                                MUTE_TIME = datetime.datetime.now() + datetime.timedelta(minutes=int(mute_time))
                                mute_list.append('{}/{}'.format(mute_site.strip(), mute_sku.strip()))
                            print('MUTE TIME: ', MUTE_TIME)
                        print(mute_list)

                    if msg.content.startswith('!screen'):
                        screenshot()

        except Exception as e:
            print(f'Error: {e}')

    client.run(token)


discord_bot()
