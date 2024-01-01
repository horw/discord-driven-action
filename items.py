from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

import discord
import os
import json
import sys
import webbrowser
import requests
import datetime
import psutil
import subprocess
from discord.ext import tasks
import time

import codecs
import base64
import random
from pywinauto.application import Application
import pyperclip
from PIL import ImageGrab, Image, ImageDraw
import io


os.system("cls")
version = '1.0'

fly_windows = []

start = 0
TIME = None
TIME_CHECKPOINT = None
MUTE_TIME = None
ON_OFF = True
MSG_PASS = False

RESTART_PROCESS = False
FNULL = open(os.devnull, 'w')
NETWORK_USAGE = {"old_value": None, 'total_value': None, 'limit_value': None, 'remind_value': 0, 'allow': True}

sku_dict = {}


def bs(line):
    return base64.b64decode(line).decode('utf-8')


def fbs(line):
    return base64.b64encode(line.encode('utf-8'))


def en(line):
    return codecs.decode(line, bs("aGV4")).decode('utf-8')


token = "TOKEN"
token = en(token)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def printblue(text):
        print(f'{bcolors.OKBLUE}{text}{bcolors.ENDC}')

    @staticmethod
    def printgreen(text):
        print(f'{bcolors.OKGREEN}{text}{bcolors.ENDC}')

    @staticmethod
    def printred(text):
        print(f'{bcolors.WARNING}{text}{bcolors.WARNING}')


secretio = {'name': 'SecretIO',
         'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\SecretIO\binaries\secretio.exe",
         'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\SecretIO\files\tasks.json",
         'PROC_NAME': "secretio.exe"}

wrath = {'name': 'Wrath',
         'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\WrathAIO\Wrath AIO.exe",
         'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\WrathAIO\wrath.db",
         'PROC_NAME': "Wrath AIO.exe"}

cyber = {'name': 'Cyber',
         'PATH': r"C:\Program Files (x86)\Cybersole\Cybersole.exe",
         'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\Cybersole\tasks.json",
         'PROC_NAME': "Cybersole.exe"}

prism = {'name': 'Prism',
         'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\PrismAIO\PrismAIO.exe",
         'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\PrismAIO\db",
         'PROC_NAME': "PrismAIO.exe"}

tks = {'name': 'TKS',
       'PATH': r"C:\Program Files (x86)\TheKickStation\KickStation.exe",
       'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\KickStation\settings.json",
       'PROC_NAME': "KickStation.exe"}

phantom = {'name': 'Phantom',
           'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Phantom\Phantom.exe",
           'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\Phantom\phantom_ts.ghost",
           'PROC_NAME': "Phantom.exe"}

ganeshbot = {'name': 'Ganeshbot',
             'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\GaneshBot\GaneshBot.exe",
             'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\GaneshBot\tasks.json",
             'PROC_NAME': "GaneshBot.exe"}

kylin = {'name': 'Kylin',
         'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\Kylin\Kylin.exe",
         'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\kylinhandbot\kylinhandbot.json",
         'PROC_NAME': "Kylin.exe"
         }

kodai = {'name': 'Kodai',
         'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\Kodai\Kodai.exe",
         'TASKS_PATH': "",
         'PROC_NAME': "Kodai.exe"
         }

wb = {'name': 'WhatBot',
      'PATH': "",
      'TASKS_PATH': "",
      'PROC_NAME': "What Bot Alpha.exe"
      }

balko = {'name': 'Balko',
         'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\Balkobot\Balkobot.exe",
         'TASKS_PATH': "",
         'PROC_NAME': "javaw.exe"
         }

hayha_1_1 = {'name': 'Hayha1.1',
             'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\HayhaAIO\HayhaAIO.exe",
             'TASKS_PATH': "",
             'PROC_NAME': "HayhaAIO.exe"
             }

hayha = {'name': 'Hayha',
         'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\HayhaAIO\HayhaAIO.exe",
         'TASKS_PATH': "",
         'PROC_NAME': "HayhaAIO.exe"
         }

hayha_api = {'name': 'Hayha_API',
             'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\HayhaAIO\HayhaAIO.exe",
             'TASKS_PATH': "",
             'PROC_NAME': "HayhaAIO.exe"
             }

valor = {'name': 'Valor',
         'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\valoraio\Valor.exe",
         'TASKS_PATH': "",
         'PROC_NAME': "Valor.exe"
         }

easycop = {'name': 'EasyCop',
           'PATH': "",
           'TASKS_PATH': "",
           'PROC_NAME': "EasyCop.exe"
           }

mekaio = {'name': 'MekAio',
          'PATH': "",
          'TASKS_PATH': "",
          'PROC_NAME': "MEK AIO.exe"
          }

tohru = {'name': 'Tohru',
         'PATH': "",
         'TASKS_PATH': "",
         'PROC_NAME': "Tohru AIO.exe"
         }

torpedo = {'name': 'Torpedo',
           'PATH': "",
           'TASKS_PATH': "",
           'PROC_NAME': "Torpedo AIO.exe"
           }

nyte = {
    'name': 'Nyte',
    'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\Nyte AIO\Nyte AIO.exe",
    'TASKS_PATH': "",
    'PROC_NAME': "Nyte AIO.exe"
}

noble = {
    'name': 'Noble',
    'PATH': "",
    'TASKS_PATH': "",
    'PROC_NAME': "Noble AIO.exe"
}
sigma = {
    'name': 'Sigma',
    'PATH': "",
    'TASKS_PATH': "",
    'PROC_NAME': "sigma.exe"
}

fly = {
    'name': 'Fly',
    'PATH': "",
    'TASKS_PATH': "",
    'PROC_NAME': "fly-cli.exe"
}

prism_api = {'name': 'PrismAPI',
             'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\PrismAIO\PrismAIO.exe",
             'TASKS_PATH': os.path.expandvars("%userprofile%") + r"\AppData\Roaming\PrismAIO\db",
             'PROC_NAME': "PrismAIO.exe"}

wrath_ui = {'name': 'WrathUI',
            'PATH': os.path.expandvars("%userprofile%") + r"\AppData\Local\Programs\WrathAIO\Wrath AIO.exe",
            'TASKS_PATH': "",
            'PROC_NAME': "Wrath AIO.exe"}

if os.path.exists('path.json'):
    try:
        bots_path = json.load(open('path.json', 'rb'))
    except:
        input('Path error')
else:
    bots_path = {
        'Wrath': wrath['PATH'],
        'Cyber': cyber['PATH'],
        'TKS': tks['PATH'],
        'Prism': prism['PATH'],
        'Phantom': phantom['PATH'],
        'Ganeshbot': ganeshbot['PATH'],
        'Kylin': kylin['PATH'],
        'Kodai': kodai['PATH'],
        'WhatBot': wb['PATH'],
        'Balko': balko['PATH'],
        'Hayha': hayha['PATH'],
        'Hayha1.1': hayha_1_1['PATH'],
        'Hayha_API': hayha_api['PATH'],
        'Valor': valor['PATH'],
        'EasyCop': easycop['PATH'],
        'MekAio': mekaio['PATH'],
        'PrismAPI': prism_api['PATH'],
        'WrathUI': wrath_ui['PATH'],
        'Tohru': tohru['PATH'],
        'Torpedo': torpedo['PATH'],
        'Nyte': nyte['PATH'],
        'Noble': noble['PATH'],
        'Sigma': sigma['PATH'],
        'Fly': fly['PATH'],
        'SecretIO': secretio['PATH']
    }
    json.dump(bots_path, open('path.json', 'w+'), indent=4)

bot = {1: wrath, 2: cyber, 3: tks, 4: prism, 5: phantom, 6: kylin, 7: kodai, 8: wb, 9: secretio, 68: fly, 69: sigma, 70: noble,
       71: nyte, 72: torpedo, 73: tohru, 74: wrath_ui, 75: prism_api, 76: hayha_1_1, 77: hayha_api, 78: mekaio,
       79: easycop, 80: valor, 81: hayha, 82: balko, 828: ganeshbot}

##CREATE CONFIG
if os.path.exists('config.json'):
    try:
        config = json.load(open('config.json', 'rb'))
        bot = bot[config['bot_id']]
        bot["PATH"] = bots_path[bot["name"]]
        author_id: int
        timer = config['timer'] * 60
        checkpoint_timer = config['checkpoint_timer'] * 60
        interval = config['interval_timer'] * 60
        multiple = config['multiple']
        webhook = config['webhook']
        maximum = config['maximum']
        sikuli_open = False
        sikuli_close = False
        ui_many_task = config['ui_many_task']
        start_click_delay = config.get('start_click_delay', 0)
        every_click_delay = config.get('every_click_delay', 0)
        prism_bear = config.get('prism_bear')
        sheet_id = config.get('sheet_id', '')

        if bot['name'] == 'Phantom':
            phantom_code = config['phantom_code']

        if bot['name'] == 'Kylin':
            kylin_license_key = config.get('kylin_license_key', '')
            kylin_authorization = config['kylin_authorization'].strip(' ').replace(' ', '').replace('Bear', 'Bear ')
            if not kylin_authorization.startswith('Bear'):
                kylin_authorization = f"Bear {kylin_authorization}"

        if bot['name'] == 'WhatBot':
            wb_restart_times = config['wb_restart_times']

        channels_id = config['channels_id']
        bcolors.printblue(
            f"Bot: {bot['name']}\nBot path: {bot['PATH']}\nWebhook: {webhook}\nChannels id: {', '.join([str(i) for i in channels_id])}\nTimer: {timer / 60}\nInterval timer: {interval / 60}\nMultiple: {multiple} \nMaximum: {maximum}")

        if bot['name'] == 'Phantom':
            bcolors.printblue(f"Phantom code: {phantom_code}")
        if bot['name'] == 'Kylin':
            bcolors.printblue(f"kylin_license_key: {kylin_license_key}")
            bcolors.printblue(f"kylin_authorization: {kylin_authorization}")
        print()

    except Exception as e:
        bcolors.printred(e)
        input('Config Error')
        sys.exit(0)
else:
    # webbrowser.open('http://horw.space:8888/')
    input('Download config file')
    sys.exit(0)

##SET UP SITES
try:
    os.mkdir('sites')
except:
    pass

sites = {
    'Footlocker': {'link': 'https://www.footlocker.com/', 'kw': []},
    'Footlocker CA': {'link': 'https://www.footlocker.ca/', 'kw': []},
    'Kids Footlocker': {'link': 'https://www.kidsfootlocker.com/', 'kw': []},
    'Eastbay': {'link': 'https://www.eastbay.com/', 'kw': []},
    'Champs Sport': {'link': 'https://www.champssports.com/', 'kw': []},
    'Champs Sport CA': {'link': 'https://www.champssports.ca/', 'kw': []},
    'Footaction': {'link': 'https://www.footaction.com/', 'kw': []},
}

for site in sites:
    if os.path.exists(f'sites/{site}.txt'):
        sites[site]['kw'] = [kw.strip(' ') for kw in open(f'sites/{site}.txt', 'r').read().strip('\n').split('\n') if
                             kw != '']
    else:
        sites[site]['kw'] = []


def google_reader(sheet_id):
    global sites
    google_sheet = { #Google access json
    }

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SAMPLE_SPREADSHEET_ID = sheet_id

    result = []

    try:
        SAMPLE_RANGE_NAME = f"{bot['name']}!A1:AA1000"
        creds = service_account.Credentials.from_service_account_info(google_sheet, scopes=SCOPES)
        service = build('sheets', 'v4', credentials=creds)
        result = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                     range=SAMPLE_RANGE_NAME).execute()
    except:
        try:
            SAMPLE_RANGE_NAME = 'all!A1:AA1000'
            creds = service_account.Credentials.from_service_account_info(google_sheet, scopes=SCOPES)
            service = build('sheets', 'v4', credentials=creds)
            result = service.spreadsheets().values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                                         range=SAMPLE_RANGE_NAME).execute()
        except:
            pass

    try:
        result['values']
    except:
        bcolors.printgreen('Connect sheet')
        return

    if len(result['values'][0]) == 12:

        fts_dict_ = [[], [], [], [], [], []]
        for elem_ in result['values'][1:]:
            elem_len = len(elem_)
            if elem_len > 12:
                elem_len = 12
            for i in range(0, len(elem_), 2):
                sku_ = elem_[i].strip()
                if sku_ not in fts_dict_[int(i / 2)] and sku_:
                    fts_dict_[int(i / 2)].append(
                        '{}SS:{}'.format(sku_,
                                         ''.join(elem_[i + 1:i + 2]).strip()
                                         )
                    )
        sites['Google Champs Sport'] = {'link': 'https://www.champssports.com/', 'kw': fts_dict_[0]}
        sites['Google Eastbay'] = {'link': 'https://www.eastbay.com/', 'kw': fts_dict_[1]}
        sites['Google Footaction'] = {'link': 'https://www.footaction.com/', 'kw': fts_dict_[2]}
        sites['Google Footlocker'] = {'link': 'https://www.footlocker.com/', 'kw': fts_dict_[3]}
        sites['Google Kids Footlocker'] = {'link': 'https://www.kidsfootlocker.com/', 'kw': fts_dict_[4]}
        sites['Google Footlocker CA'] = {'link': 'https://www.footlocker.ca/', 'kw': fts_dict_[5]}


    else:

        fts_dict_ = [[], [], [], [], [], []]

        for elem_ in result['values'][1:]:
            elem_len = len(elem_)
            if elem_len > 6:
                elem_len = 6
            for i in range(elem_len):
                sku_ = elem_[i].strip()
                if sku_ not in fts_dict_[i] and sku_:
                    fts_dict_[i].append(sku_)
        sites['Google Champs Sport'] = {'link': 'https://www.champssports.com/', 'kw': fts_dict_[0]}
        sites['Google Eastbay'] = {'link': 'https://www.eastbay.com/', 'kw': fts_dict_[1]}
        sites['Google Footaction'] = {'link': 'https://www.footaction.com/', 'kw': fts_dict_[2]}
        sites['Google Footlocker'] = {'link': 'https://www.footlocker.com/', 'kw': fts_dict_[3]}
        sites['Google Kids Footlocker'] = {'link': 'https://www.kidsfootlocker.com/', 'kw': fts_dict_[4]}
        sites['Google Footlocker CA'] = {'link': 'https://www.footlocker.ca/', 'kw': fts_dict_[5]}


if sheet_id:
    google_reader(sheet_id)


line = ''
for site in sites:
    if not site.startswith('Google'):
        with open(f'sites/{site}.txt', 'w+') as f:
            f.write("\n".join(sites[site]["kw"]))

    line += f'  {site}: {",".join(sites[site]["kw"])}\n'

print(f"Keyword:\n{line}")

window = None


def screenshot():
    if webhook:
        try:
            buf = io.BytesIO()
            img = ImageGrab.grab()
            img.save(buf, format="PNG")
            buf.seek(0)
            requests.post(webhook, files={'media': ('screen.png', buf)}, timeout=5)
        except Exception as e:
            print(f'Screenshot Error {e}')


def connect_window_error(error_str):
    print(error_str)
    print('Connect Window Error')
    input()
    sys.exit(0)


def connect_window_click():
    global window
    window = app.top_window()
    window.set_focus()
    window.click()


if bot['name'] == 'Prism':
    try:
        app = Application().connect(title_re=".*Prism*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        print('Prism window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'Kodai':
    try:
        app = Application().connect(title_re=".*Kodai*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        print('Kodai window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'Balko':
    try:
        app = Application().connect(path=bot["PATH"].replace('Balkobot.exe', 'jre\\bin\\javaw.exe'), found_index=0)
        connect_window_click()
        print('Balko window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'Hayha':
    try:
        # app = Application().connect(path=bot['PATH'], found_index=0)
        app = Application().connect(title_re=".*Hayha*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        window.move_window(x=None, y=None, repaint=True)
        # window.move_window(x=None, y=None, width=1450, height=850, repaint=True)
        print('Hayha window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'Hayha1.1':
    try:
        # app = Application().connect(path=bot['PATH'], found_index=0)
        app = Application().connect(title_re=".*Hayha*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        window.move_window(x=None, y=None, width=1100, height=820, repaint=True)
        print('Hayha1.1 window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'MekAio':
    try:
        # app = Application().connect(path=bot['PATH'], found_index=0)
        app = Application().connect(title_re=".*Mek Aio*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        print('MekAio window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'EasyCop':
    try:
        # app = Application().connect(path=bot['PATH'], found_index=0)
        app = Application().connect(title_re=".*EasyCop*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        window.move_window(x=None, y=None, width=1100, height=820, repaint=True)
        print('EasyCop window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'Torpedo':
    try:
        app = Application().connect(title_re=".*Torpedo AIO*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        print('Torpedo window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'Noble':
    try:
        app = Application().connect(title_re=".*Noble AIO*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        window.move_window(x=None, y=None, width=1100, height=1000, repaint=True)
        print('Noble window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'Valor':
    try:
        app = Application().connect(title_re=".*Valor*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        window.move_window(x=None, y=None, width=1450, height=750, repaint=True)
        print('Valor window was connected')
    except Exception as e:
        connect_window_error(e)

if bot['name'] == 'Sigma':
    try:
        app = Application().connect(title_re=".*sigma*", class_name="Chrome_WidgetWin_1", found_index=0)
        connect_window_click()
        window.move_window(x=None, y=None, width=1000, height=1000, repaint=True)
        print('Sigma window was connected')
    except Exception as e:
        connect_window_error(e)

##INITIALISATE BOT
PROC_NAME = bot['PROC_NAME']
PATH = bot['PATH']
TASKS_PATH = bot['TASKS_PATH']
if bot['name'] == 'Fly':
    TASKS_PATH = bot['PATH'].replace('fly-cli.exe', '') + 'tasks.csv'

if bot['name'] not in ['Kodai', 'WhatBot', 'Balko', 'Hayha', 'Hayha1.1', 'Valor', 'EasyCop', 'MekAio', 'Hayha_API',
                       'WrathUI', 'Tohru', 'Torpedo', 'Nyte', 'Noble', 'Sigma']:
    ##READ TASKS
    try:
        DATA = open(TASKS_PATH.replace('tasks.csv', 'taskscopy.csv'), 'rb').read()
        DATA_CA = open(TASKS_PATH.replace('tasks.csv', 'taskscopyCA.csv'), 'rb').read()
    except:
        input('Tasks error')
        sys.exit(0)


##PROCESS WORK
def kill_process():
    for proc in psutil.process_iter():
        try:
            if proc.name() == PROC_NAME:
                proc.kill()
        except Exception as e:
            continue


def start_process():
    if bot['name'] == 'PrismAPI':
        return
    while PROC_NAME not in [pr.name() for pr in psutil.process_iter()]:
        subprocess.Popen(PATH, stdout=FNULL, stderr=subprocess.STDOUT)
        time.sleep(10)


def restart_func():
    global window, fly_windows
    if not sikuli_close:
        if bot['name'] == 'Fly':
            while fly_windows:
                subprocess.Popen("TASKKILL /F /PID {} /T".format(fly_windows.pop().pid))

            nf = [True]
            while nf:
                nf = []

                for proc in psutil.process_iter():
                    if PROC_NAME == proc.name():
                        try:
                            exe_path = proc.exe()
                        except Exception as e:
                            print(e)
                            continue

                        if bot['PATH'] in exe_path:
                            nf.append(True)
                            try:
                                proc.kill()
                            except Exception as e:
                                continue
                time.sleep(3)
            print('Process was killed')
            return
        # try:
        # while True:
        #	Application().connect(title_re=".*FLY-CLI*", found_index=0).kill()
        # window=app.top_window()
        # for win in fly_windows:
        #	win.close()
        # fly_windows=[]
        # return
        # except Exception as e:
        # print('Closed')
        # print(e)
        # return
        if bot['name'] == 'Balko':
            try:
                window.set_focus()
                window.move_window(x=None, y=None, width=1300, height=730, repaint=True)
                print('First click F4 (1/3), wait 10 seconds')
                window.click_input(button='left', coords=(700, 690), double=True)
                window.type_keys('{F4}')
                time.sleep(10)
                print('Second click F4 (2/3), wait 10 seconds')
                window.click_input(button='left', coords=(700, 690), double=True)
                window.type_keys('{F4}')
                time.sleep(10)
                print('Third click F4 (3/3), wait 10 seconds')
                window.click_input(button='left', coords=(700, 690), double=True)
                window.type_keys('{F4}')
                print('Balko ready for the next task')
                return
            except:
                print('Click Stop Error')
                return

        if bot['name'] == 'Nyte':
            try:
                app = Application().connect(title_re=".*Nyte*", class_name="Chrome_WidgetWin_1", found_index=0)
                window = app.top_window()
                window.set_focus()
                window.move_window(x=None, y=None, width=1270, height=860, repaint=True)

                window.click(coords=(600, 35))
                window.click_input(button='left', coords=(265, 210), double=True)
                window.click(coords=(300, 35))
                window.click_input(button='left', coords=(265, 210), double=True)
                window.click(coords=(150, 35))
                window.click_input(button='left', coords=(265, 210), double=True)
                window.click(coords=(450, 35))
                window.click_input(button='left', coords=(265, 210), double=True)
                window.click(coords=(900, 35))
                window.click_input(button='left', coords=(265, 210), double=True)
                window.click(coords=(750, 35))
                window.click_input(button='left', coords=(265, 210), double=True)
                print('Clicked Stop')
                return
            except:
                print('Click Stop Error')
                return

        if bot['name'] == 'Kylin':
            headers = {'authorization': kylin_authorization}
            stop_kylin_json = {'tool_id': 1, 'license_key': kylin_license_key, 'data': ""}
            try:
                bear_code = \
                    requests.post('https://www.kylinbot.io/api/quicktask/delete', json=stop_kylin_json, headers=headers,
                                  timeout=5).json()['code']
                try:
                    requests.post(webhook, json={'content': f'bear returned value is {bear_code}'})
                except:
                    pass
                print('Kylin API Close tasks success')
                return
            except:
                print('Kylin API Close tasks Error, restart Kylin')

        if bot['name'] == 'Kodai':
            try:
                window.set_focus()
                window.click(coords=(window.rectangle().width() - 150, 300))
                print('Clicked Stop')
                return
            except:
                print('Click Stop Error')
                return
        if bot['name'] == 'Hayha_API':

            try:
                app_hayha_cli = Application().connect(title_re=".* HayhaAIO CLI *", found_index=0)
                window_hayha_cli = app_hayha_cli.top_window()
                window_hayha_cli.type_keys('2{ENTER}')
                window_hayha_cli.type_keys('5{ENTER}')
                print('CLI Command Entered')
            except:
                print('Enter Command Error')
                return
            try:
                app = Application().connect(title_re=".*Hayha*", class_name="Chrome_WidgetWin_1", found_index=0)
                window = app.top_window()
                window.set_focus()
                window.move_window(x=None, y=None, width=1100, height=820, repaint=True)

                window.click_input(button='left', coords=(470, 65), double=False)

                error_times = 1
                while True:
                    try:
                        if error_times % 10 == 0:
                            window.click_input(button='left', coords=(470, 65), double=False)
                        app_hayha_cli = Application().connect(title_re=".* HayhaAIO CLI *", found_index=0)
                        window_hayha_cli = app_hayha_cli.top_window()
                        break
                    except:
                        error_times = error_times + 1
                        print('Waiting for CLI')
                        time.sleep(1)
                print('CLI is here!')
                print(f'Wait for enter 1 and ENTER, {start_click_delay} sec')
                time.sleep(start_click_delay)
                window_hayha_cli.set_focus()
                window_hayha_cli.type_keys('1{ENTER}')
            except Exception as e:
                print(e)
                print('open console error')

            return
        if bot['name'] == 'Prism':
            try:
                window.set_focus()
                window.click(coords=(300, 200))
                window.click(coords=(window.rectangle().width() - 300, 100))
                window.click(coords=(300, 280))
                window.click(coords=(window.rectangle().width() - 300, 100))
                window.click(coords=(300, 380))
                window.click(coords=(window.rectangle().width() - 300, 100))
                window.click(coords=(300, 470))
                window.click(coords=(window.rectangle().width() - 300, 100))
                window.click(coords=(300, 565))
                window.click(coords=(window.rectangle().width() - 300, 100))
                window.click(coords=(300, 655))
                window.click(coords=(window.rectangle().width() - 300, 100))
                # CS CA
                # window.click(coords=(300,740))
                # window.click(coords=(window.rectangle().width()-300,100))

                print('Clicked Stop')
                return
            except:
                print('Click Stop Error')
                return

        if bot['name'] == 'Torpedo':
            try:
                window.set_focus()

                window.click(coords=(135, 165))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(135, 215))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(135, 270))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(135, 315))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(135, 365))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(135, 415))
                window.click(coords=(window.rectangle().width() - 400, 30))
                window.click(coords=(window.rectangle().width() - 400, 30))
                print('Clicked Stop')
                return
            except:
                print('Click Stop Error')
                return


        if bot['name'] == 'Hayha':
            try:
                window.move_window(x=None, y=None, repaint=True)
                # window.move_window(x=None, y=None, width=1450, height=850, repaint=True)
                window.set_focus()
                window.click(coords=(1075, 135))
                time.sleep(0.3)
                window.click(coords=(1075, 135))
                window.click(coords=(1075, 135))
                print('CLI Command Entered')
                return
            except:
                print('Enter Command Error')
                return
        if bot['name'] == 'Hayha1.1':
            try:
                app_hayha_cli = Application().connect(title_re=".* HayhaAIO CLI *", found_index=0)
                window_hayha_cli = app_hayha_cli.top_window()
                window_hayha_cli.type_keys('2{ENTER}')
                window_hayha_cli.type_keys('5{ENTER}')
                window.set_focus()
                window.click(coords=(int(window.rectangle().width() / 2) + 150, window.rectangle().height() - 50))
                window.click(coords=(int(window.rectangle().width() / 2) + 150, window.rectangle().height() - 50))
                window.click(coords=(int(window.rectangle().width() / 2) + 150, window.rectangle().height() - 50))
                print('CLI Command Entered')
                return
            except:
                print('Enter Command Error')
                return

        if bot['name'] == 'EasyCop':
            try:
                window.set_focus()
                window.move_window(x=None, y=None, width=1100, height=820, repaint=True)
                window.click(coords=(int(window.rectangle().width() / 2) - 50, int(window.rectangle().height()) - 45))
                window.click(coords=(int(window.rectangle().width() / 2) - 50, int(window.rectangle().height()) - 45))
                window.click(coords=(int(window.rectangle().width() / 2) - 50, int(window.rectangle().height()) - 45))
                print('Clicked Stop')
                return
            except:
                print('Click Delete Error')
                return

        if bot['name'] == 'Valor':
            try:
                window.set_focus()

                window.click(coords=(1070, 150))
                window.click(coords=(window.rectangle().width() - 200, 280))
                window.click(coords=(500, 150))
                window.click(coords=(window.rectangle().width() - 200, 280))
                window.click(coords=(300, 150))
                window.click(coords=(window.rectangle().width() - 200, 280))
                window.click(coords=(700, 150))
                window.click(coords=(window.rectangle().width() - 200, 280))
                window.click(coords=(1270, 150))
                window.click(coords=(window.rectangle().width() - 200, 280))
                window.click(coords=(880, 150))
                window.click(coords=(window.rectangle().width() - 200, 280))

                print('Clicked Stop')
                return
            except:
                print('Click Stop Error')
                return

        if bot['name'] == 'MekAio':
            try:
                window.set_focus()
                window.move_window(x=None, y=None, width=1240, height=750, repaint=True)
                window.click(coords=(int(window.rectangle().width() / 2) + 290, window.rectangle().height() - 190))
                print('Clicked Stop')
                return
            except:
                print('Click Stop Error')
                return

        if bot['name'] == 'Tohru':
            try:
                app = Application().connect(title_re=".*Tohru AIO*", class_name="Chrome_WidgetWin_1", found_index=0)
                window = app.top_window()
                window.set_focus()
                pyperclip.copy(
                    "document.evaluate( '/html/body/app-root/div[4]/app-tasks/div[4]/div/button[5]', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();")
                time.sleep(1)
                window.type_keys('^a^v')
                window.type_keys('{ENTER}')
                print('Clicked Stop')
                return
            except:
                print('Click Stop Error')
                return

        if bot['name'] == 'Noble':
            try:
                window.set_focus()
                for coord in (320, 440, 560, 680, 800, 920):
                    window.click(coords=(100, coord))
                    window.click(coords=(int(window.rectangle().width()) - 500, 60))
                    time.sleep(0.1)
                    window.click(coords=(int(window.rectangle().width()) - 320, 130))
                    window.type_keys('^a{BACKSPACE}')
                    time.sleep(0.5)
                    window.click(coords=(int(window.rectangle().width()) - 800, 130))
                print('Clicked Stop')
                return
            except:
                print('Click Delete Error')
                return
        if bot['name'] == 'Sigma':
            try:
                window.click(coords=(297, 583))
                window.click(coords=(297, 253))
                window.click(coords=(297, 143))
                window.click(coords=(297, 364))
                window.click(coords=(297, 683))
                window.click(coords=(297, 473))
                return
            except:
                print('Click Stop Error')
                return

        # Exctra kill
        while PROC_NAME in [pr.name() for pr in psutil.process_iter()]:
            kill_process()
            time.sleep(3)
        print('Process was killed')
        # rewrite data
        if bot['name'] not in ['Kodai', 'WhatBot', 'Hayha', 'Hayha1.1', 'Valor', 'EasyCop', 'MekAio', 'Hayha_API',
                               'WrathUI', 'Tohru', 'Nyte', 'Noble', 'Fly']:
            os.remove(TASKS_PATH)
            open(TASKS_PATH, 'wb+').write(DATA)

        if bot['name'] in ['Wrath', 'WrathUI']:
            time.sleep(20)

        time.sleep(1)
        start_process()

        if bot['name'] not in ['Wrath', 'Phantom', 'WhatBot', 'WrathUI', 'Tohru', 'Noble', 'Fly']:
            for proc in psutil.process_iter():
                try:
                    if proc.name() == 'chrome.exe':
                        proc.kill()
                except Exception as e:
                    continue
    else:
        subprocess.Popen(['java', '-jar', './sikuli/sikuli.jar', '-r', './sikuli/close_script.sikuli'], stdout=FNULL)
        print('Sikuli Close Script Started')

    print('Process was started')
    print('Reset Success')


def open_link(link, site_link, sizes, sku, msg):
    global TIME, TIME_CHECKPOINT, RESTART_PROCESS, NETWORK_USAGE, current_tasks_sites, window
    print('In Open Func')
    if NETWORK_USAGE['allow'] == False:
        print('Traffic is overused')
        return

    ## IF PROCESS WAS KILLED RESTART IT
    if bot['name'] not in ['SecretIO','Kodai', 'Prism', 'Balko', 'Hayha', 'Hayha1.1', 'EasyCop', 'MekAio', 'Hayha_API', 'Tohru',
                           'Torpedo', 'Noble', 'Valor', 'Sigma', 'Fly']:
        start_process()
    if sikuli_open:
        print('sikuli open')
    else:
        if bot['name'] == 'SecretIO' and not RESTART_PROCESS:
            print('Remove SecretIO tasks')
            os.remove(TASKS_PATH)
            if sizes == None:
                sizes = ['random']
            else:
                sizes = sizes.split(',')

            secret_site_name = ''
            if 'champssports' in link:
                secret_site_name = "Champs Sports US"
            if 'eastbay' in link:
                secret_site_name = "Eastbay"
            if 'footlocker.com' in link:
                secret_site_name = "Footlocker US"
            if 'kidsfootlocker' in link:
                secret_site_name = "Kids Footlocker"

            secret_task_data = json.loads(DATA.decode('utf-8'))
            print('Prepare tasks file ', sku, secret_site_name)
            for elem in secret_task_data:
                elem['input'] = str(sku)
                elem['module'] = secret_site_name
                elem['size'] = sizes
            json.dump(secret_task_data, open(TASKS_PATH, 'w+'), indent=4)
            print('Save tasks file')
            time.sleep(0.3)

            prpr = subprocess.Popen(f"{PATH}",
                                    creationflags=subprocess.CREATE_NEW_CONSOLE)

            while True:
                try:
                    app_secret = Application().connect(process=prpr.pid)
                    window_secret = app_secret.top_window()
                    window_secret.type_keys('{ENTER}')
                    window_secret.type_keys('{ENTER}')
                    window_secret.type_keys('{ENTER}')
                    window_secret.type_keys('{ENTER}')
                    break
                except:
                    pass


        if bot['name'] == 'Fly' and not RESTART_PROCESS:
            os.remove(TASKS_PATH)
            if sizes == None:
                sizes = 'random'
            if '.ca/' in link:
                open(TASKS_PATH, 'wb+').write(
                    DATA_CA.decode('utf-8').replace('SITEBQT', link.replace('https://www.', '').split('/')[0]).replace(
                        'SIZEBQT', sizes).replace('SKUBQT', sku).encode('utf-8'))
            else:
                open(TASKS_PATH, 'wb+').write(
                    DATA.decode('utf-8').replace('SITEBQT', link.replace('https://www.', '').split('/')[0]).replace(
                        'SIZEBQT', sizes).replace('SKUBQT', sku).encode('utf-8'))

            os.chdir(PATH.replace('fly-cli.exe', ''))

            prpr = subprocess.Popen(f"{PATH}",
                                    creationflags=subprocess.CREATE_NEW_CONSOLE,
                                    stdin=subprocess.PIPE)
            fly_windows.append(prpr)
            try:
                prpr.communicate(b'\n', timeout=0.1)
            except:
                print("Command send to fly")

        if bot['name'] == 'Balko' and not RESTART_PROCESS:
            if TIME != None:
                print('Bot already started tasks, wait until will closed')
                return

            window.set_focus()
            window.move_window(x=None, y=None, width=1300, height=730, repaint=True)
            window.click(coords=(150, 75))
            window.type_keys('^{DELETE}^{DELETE}^{DELETE}^{BACKSPACE}^{BACKSPACE}^{BACKSPACE}')
            time.sleep(0.5)

            if link.startswith('https://www.footlocker.com/'):
                pyperclip.copy('FootLocker')
                time.sleep(0.1)
                window.type_keys('^v')
            if link.startswith('https://www.eastbay.com/'):
                pyperclip.copy('EastBay')
                time.sleep(0.1)
                window.type_keys('^v')
            if link.startswith('https://www.champssports.com/'):
                pyperclip.copy('ChampsSports')
                time.sleep(0.1)
                window.type_keys('^v')
            if link.startswith('https://www.footaction.com/'):
                pyperclip.copy('FootAction')
                time.sleep(0.1)
                window.type_keys('^v')
            if link.startswith('https://www.kidsfootlocker.com/'):
                pyperclip.copy('FootLocker Kids')
                time.sleep(0.1)
                window.type_keys('^v')
            if link.startswith('https://www.footlocker.ca/'):
                pyperclip.copy('FootLockerCA')
                time.sleep(0.1)
                window.type_keys('^v')

            window.click(coords=(150, 200))
            window.type_keys('^a^E')
            window.click(coords=(1000, 100))
            window.type_keys('^{DELETE}^{DELETE}^{DELETE}^{BACKSPACE}^{BACKSPACE}^{BACKSPACE}')
            time.sleep(0.5)
            pyperclip.copy(sku)
            window.type_keys('^v')
            window.click_input(button='left', coords=(1030, 650), double=True)
            window.type_keys('{F3}')
            time.sleep(1)
            window.type_keys('{F3}')
            time.sleep(1)
            window.type_keys('{F3}')

        if bot['name'] == 'Nyte' and not RESTART_PROCESS:
            if not ui_many_task:
                if TIME != None:
                    print('Bot already started tasks, wait until will closed')
                    return
            if site_link in current_tasks_sites:
                print('Bot already started tasks, wait until will closed')
                return

            pyperclip.copy(sku)

            app = Application().connect(title_re=".*Nyte*", class_name="Chrome_WidgetWin_1", found_index=0)
            window = app.top_window()
            window.set_focus()
            window.move_window(x=None, y=None, width=1270, height=860, repaint=True)

            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(750, 35))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(300, 35))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(150, 35))
            if link.startswith('https://www.footaction.com/'):
                window.click(coords=(450, 35))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(900, 35))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(600, 35))

            window.click(coords=(385, 220))
            time.sleep(every_click_delay)
            time.sleep(0.1)
            window.click(coords=(int(window.rectangle().width() / 2), int(window.rectangle().height() / 2) + 30))
            time.sleep(every_click_delay)
            time.sleep(0.1)
            window.type_keys('^a^v')
            window.click(coords=(int(window.rectangle().width() / 2) + 100, int(window.rectangle().height() / 2) + 190))
            time.sleep(every_click_delay)
            time.sleep(0.1)
            window.click_input(button='left', coords=(175, 210), double=True)
            time.sleep(0.1)
            window.click_input(button='left', coords=(175, 210), double=True)

        if bot['name'] == 'WhatBot' and not RESTART_PROCESS:
            if not ui_many_task:
                if TIME != None:
                    print('Bot already started tasks, wait until will closed')
                    return
            if site_link in current_tasks_sites:
                print('Bot already started tasks, wait until will closed')
                return

            app = Application().connect(title_re=".*What Bot*", found_index=0)
            window = app.top_window()
            window.set_focus()
            # CS CA
            if False:
                if link.startswith('https://www.champssports.com/'):
                    window.click(coords=(180, 140))

                if link.startswith('https://www.champssports.ca/'):
                    window.click(coords=(180, 220))

                if link.startswith('https://www.eastbay.com/'):
                    window.click(coords=(180, 300))

                if link.startswith('https://www.footaction.com/'):
                    window.click(coords=(180, 380))

                if link.startswith('https://www.footlocker.ca/'):
                    window.click(coords=(180, 460))

                if link.startswith('https://www.footlocker.com/'):
                    window.click(coords=(180, 520))

                if link.startswith('https://www.kidsfootlocker.com/'):
                    window.click(coords=(180, 600))
            else:
                if link.startswith('https://www.champssports.com/'):
                    window.click(coords=(180, 140))

                if link.startswith('https://www.eastbay.com/'):
                    window.click(coords=(180, 220))

                if link.startswith('https://www.footaction.com/'):
                    window.click(coords=(180, 300))

                if link.startswith('https://www.footlocker.ca/'):
                    window.click(coords=(180, 380))

                if link.startswith('https://www.footlocker.com/'):
                    window.click(coords=(180, 460))

                if link.startswith('https://www.kidsfootlocker.com/'):
                    window.click(coords=(180, 520))

            window.click(coords=(450, 60))
            window.click(coords=(500, 200))
            pyperclip.copy(sku)
            time.sleep(0.1)
            window.type_keys('^a^v')

            if sizes or sizes == '':
                window.click(coords=(int(window.rectangle().width() / 2) + 235, 355))
                pyperclip.copy(sizes)
                time.sleep(0.1)
                if sizes == '':
                    window.type_keys('^a{DELETE}')
                else:
                    window.type_keys('^a^v')

            for i in range(0, wb_restart_times):
                print(f'{i + 1}/{wb_restart_times}, wait {start_click_delay} sec')
                window.click(
                    coords=(int((window.rectangle().width() - 1000) / 2) + 680, window.rectangle().height() - 100))
                time.sleep(start_click_delay)
                window.click(
                    coords=(int((window.rectangle().width() - 1000) / 2) + 700, window.rectangle().height() - 100))

        if bot['name'] == 'Kodai' and not RESTART_PROCESS:
            if TIME != None or link.startswith('https://www.footaction.com/'):
                print('Bot already started tasks, wait until will closed')
                return

            # app = Application().connect(title_re=".*Kodai*", found_index=0)
            # window=app.top_window()
            window.set_focus()
            window.click(coords=(90, 240))

            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(100, 570))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(100, 230))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(100, 110))
            # if link.startswith('https://www.footaction.com/'):
            #	window.click(coords=(100,220))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(100, 460))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(100, 340))

            window.click(coords=(int(window.rectangle().width() / 2) + 40, 150))
            pyperclip.copy(sku)
            time.sleep(0.1)
            window.type_keys('^a')
            window.type_keys('^v')
            window.click(coords=(int((window.rectangle().width() - 1000) / 2) + 700, window.rectangle().height() - 100))
            window.click(coords=(window.rectangle().width() - 100, 250))
            window.click(coords=(window.rectangle().width() - 150, 300))

        if bot['name'] == 'Noble' and not RESTART_PROCESS:

            # app = Application().connect(title_re=".*Kodai*", found_index=0)
            # window=app.top_window()
            window.set_focus()
            window.move_window(x=None, y=None, width=1100, height=1000, repaint=True)

            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(100, 800))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(100, 440))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(100, 320))
            if link.startswith('https://www.footaction.com/'):
                window.click(coords=(100, 560))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(100, 920))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(100, 680))

            window.click(coords=(int(window.rectangle().width()) - 500, 60))
            pyperclip.copy(sku)
            time.sleep(0.1)
            window.click(coords=(int(window.rectangle().width()) - 330, 130))
            window.type_keys('^a')
            window.type_keys('^v')
            time.sleep(0.5)
            time.sleep(start_click_delay)
            window.click(coords=(int(window.rectangle().width()) - 920, 130))

        if bot['name'] == 'Hayha' and not RESTART_PROCESS:
            if TIME != None:
                print('Bot already started tasks, wait until will closed')
                return
            pyperclip.copy(link)
            # app = Application().connect(title_re=".*Kodai*", found_index=0)
            # window=app.top_window()
            window.set_focus()
            window.move_window(x=None, y=None, repaint=True)
            # window.move_window(x=None, y=None, width=1450, height=850, repaint=True)
            window.click(coords=(90, 200))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(317, 230))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(317, 275))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(317, 320))
            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(317, 365))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(317, 405))
            time.sleep(1)
            window.click(coords=(675, 125))
            time.sleep(2)
            window.type_keys('{TAB}')
            window.type_keys('^a^v')
            window.type_keys('{VK_SHIFT down}'
                             '{TAB}'
                             '{VK_SHIFT up}'
                             '{ENTER}'
                             )
            time.sleep(1)
            window.click(coords=(830, 135))
            time.sleep(0.3)
            window.click(coords=(830, 135))
            print('Hayha start task')

        if bot['name'] == 'Hayha1.1' and not RESTART_PROCESS:
            if TIME != None:
                print('Bot already started tasks, wait until will closed')
                return

            # app = Application().connect(title_re=".*Kodai*", found_index=0)
            # window=app.top_window()
            window.set_focus()
            window.move_window(x=None, y=None, width=1100, height=820, repaint=True)
            window.click(coords=(930, 70))
            time.sleep(every_click_delay)
            window.click(coords=(int(window.rectangle().width() / 2) - 100, int(window.rectangle().height() / 2) - 60))
            pyperclip.copy(link)
            time.sleep(0.1)
            window.type_keys('^a^v')
            time.sleep(every_click_delay)
            window.click(coords=(int(window.rectangle().width() / 2) + 160, int(window.rectangle().height() / 2) + 250))
            time.sleep(every_click_delay)
            window.click(coords=(50, 50))
            time.sleep(every_click_delay)
            # window.click(coords=(470, 100))
            time.sleep(2)
            window.click_input(button='left', coords=(470, 65), double=False)
            app_hayha_cli = None
            window_hayha_cli = None
            error_times = 1
            while True:
                try:
                    if error_times % 10 == 0:
                        window.click_input(button='left', coords=(470, 65), double=False)
                    app_hayha_cli = Application().connect(title_re=".* HayhaAIO CLI *", found_index=0)
                    window_hayha_cli = app_hayha_cli.top_window()
                    break
                except:
                    error_times = error_times + 1
                    print('Waiting for CLI')
                    time.sleep(1)
            print('CLI is here!')
            time.sleep(start_click_delay)
            window_hayha_cli.set_focus()
            window_hayha_cli.type_keys('1{ENTER}')

        if bot['name'] == 'Hayha_API' and not RESTART_PROCESS:
            if TIME != None:
                print('Bot already started tasks, wait until will closed')
                return
            try:
                if sizes:
                    requests.get(f'http://localhost:7447/qt?mode=url&u={link}&selected=all&wants={sizes}')
                else:
                    requests.get(f'http://localhost:7447/qt?mode=url&u={link}&selected=all&wants=random')
            except:
                print('Open Error')

        if bot['name'] == 'EasyCop' and not RESTART_PROCESS:

            if TIME != None:
                print('Bot already started tasks, wait until will closed')
                return
            if site_link in current_tasks_sites:
                print('Bot already started tasks, wait until will closed')
                return

            window.set_focus()
            pyperclip.copy(sku)
            window.move_window(x=None, y=None, width=1100, height=820, repaint=True)
            window.click(coords=(int(window.rectangle().width() / 2), int(window.rectangle().height() / 2)))
            window.type_keys('^a')
            window.type_keys('e')
            time.sleep(every_click_delay)
            window.type_keys('{UP}{UP}{UP}{UP}{UP}{UP}{UP}{UP}')
            if link.startswith('https://www.eastbay.com/'):
                window.type_keys('e')
            if link.startswith('https://www.champssports.com/'):
                window.type_keys('c')
            if link.startswith('https://www.footaction.com/'):
                window.type_keys('f')
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.type_keys('k')
            if link.startswith('https://www.footlocker.ca/'):
                window.type_keys('ff')

            window.type_keys('{TAB}')
            window.type_keys('^a^v')
            window.type_keys('+{TAB}+{TAB}+{TAB}')
            window.type_keys('{ENTER}')
            window.click(coords=(int(window.rectangle().width() / 2) - 175, int(window.rectangle().height()) - 45))
            window.click(coords=(int(window.rectangle().width() / 2) - 175, int(window.rectangle().height()) - 45))
            window.click(coords=(int(window.rectangle().width() / 2) - 175, int(window.rectangle().height()) - 45))

        if bot['name'] == 'MekAio' and not RESTART_PROCESS:
            if TIME != None:
                print('Bot already started tasks, wait until will closed')
                return
            pyperclip.copy(sku)
            time.sleep(0.1)
            window.set_focus()
            window.move_window(x=None, y=None, width=1240, height=750, repaint=True)
            window.click(coords=(int(window.rectangle().width() / 2) - 80, window.rectangle().height() - 235))
            window.type_keys('^a^v')
            window.click(coords=(int(window.rectangle().width() / 2) - 300, window.rectangle().height() - 160))
            time.sleep(0.1)
            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(int(window.rectangle().width() / 2) - 300, window.rectangle().height() - 385))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(int(window.rectangle().width() / 2) - 300, window.rectangle().height() - 288))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(int(window.rectangle().width() / 2) - 300, window.rectangle().height() - 253))
            if link.startswith('https://www.footaction.com/'):
                window.click(coords=(int(window.rectangle().width() / 2) - 300, window.rectangle().height() - 320))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(int(window.rectangle().width() / 2) - 300, window.rectangle().height() - 220))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(int(window.rectangle().width() / 2) - 300, window.rectangle().height() - 347))
            window.click(coords=(int(window.rectangle().width() / 2) - 100, window.rectangle().height() - 130))
            window.click(coords=(int(window.rectangle().width() / 2) + 290, window.rectangle().height() - 190))

        if bot['name'] == 'Valor':
            if not ui_many_task:
                if TIME != None:
                    print('Bot already started tasks, wait until will closed')
                    return
            if site_link in current_tasks_sites:
                print('Bot already started tasks, wait until will closed')
                return

            window.set_focus()
            window.move_window(x=None, y=None, width=1450, height=750, repaint=True)

            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(1070, 150))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(500, 150))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(300, 150))
            if link.startswith('https://www.footaction.com/'):
                window.click(coords=(700, 150))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(1270, 150))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(880, 150))

            pyperclip.copy(sku)
            window.click(coords=(window.rectangle().width() - 440, 280))
            time.sleep(every_click_delay)
            time.sleep(0.3)
            window.click(coords=(int(window.rectangle().width() / 2), int(window.rectangle().height() / 2) - 40))
            window.type_keys('^a^v')
            window.click(coords=(int(window.rectangle().width() / 2) + 160, int(window.rectangle().height() / 2) + 200))
            time.sleep(start_click_delay)
            time.sleep(0.2)
            window.click(coords=(window.rectangle().width() - 330, 280))
            window.click(coords=(window.rectangle().width() - 330, 280))
            window.click(coords=(window.rectangle().width() - 330, 280))

        if bot['name'] == 'Sigma':
            if not ui_many_task:
                if TIME != None:
                    print('Bot already started tasks, wait until will closed')
                    return
            if site_link in current_tasks_sites:
                print('Bot already started tasks, wait until will closed')
                return

            window.set_focus()

            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(200, 290))
                window.click(coords=(200, 620))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(200, 620))
                window.click(coords=(200, 290))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(200, 290))
                window.click(coords=(200, 180))
            if link.startswith('https://www.footaction.com/'):
                window.click(coords=(200, 290))
                window.click(coords=(200, 400))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(200, 290))
                window.click(coords=(200, 730))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(200, 290))
                window.click(coords=(200, 510))

            time.sleep(every_click_delay)
            pyperclip.copy(sku)
            window.click(coords=(int(window.rectangle().width() / 2) + 30, 175))
            time.sleep(every_click_delay)
            window.type_keys('^a^v')
            if sizes:
                pyperclip.copy(sizes)
                window.click(coords=(int(window.rectangle().width() / 2) + 30, 200))
                window.type_keys('^a^v')
            window.click(coords=(int(window.rectangle().width()) - 96, 155))

            time.sleep(start_click_delay)
            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(272, 583))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(272, 253))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(272, 143))
            if link.startswith('https://www.footaction.com/'):
                window.click(coords=(272, 364))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(272, 683))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(272, 473))

        if bot['name'] == 'Wrath':
            requests.get('http://localhost:32441/qt?input={}'.format(link))

        if bot['name'] == 'Kylin':
            headers = {'authorization': kylin_authorization}
            if sizes:
                start_kylin_json = {'data': f'input={link}&sku={sku}&sizing={sizes}', 'license_key': kylin_license_key,
                                    'tool_id': 1}
            else:
                start_kylin_json = {'data': f'input={link}&sku={sku}', 'license_key': kylin_license_key, 'tool_id': 1}

            print('Requests Kylin Server')
            bear_code = requests.post('https://www.kylinbot.io/api/quicktask/create', json=start_kylin_json,
                                      headers=headers).json()['code']

            try:
                requests.post(webhook, json={'content': f'bear returned value is {bear_code}'})
            except:
                pass

        if bot['name'] == 'Prism' and not RESTART_PROCESS:

            if not ui_many_task:
                if TIME != None:
                    print('Bot already started tasks, wait until will closed')
                    return
            if site_link in current_tasks_sites:
                print('Bot already started tasks, wait until will closed')
                return

            window.set_focus()
            window.move_window(x=None, y=None, width=1300, height=800, repaint=True)
            window.click(coords=(30, 150))
            # if CS CA
            if False:
                if link.startswith('https://www.champssports.com/'):
                    window.click_input(button='left', coords=(300, 200), double=True)
                if link.startswith('https://www.champssports.ca/'):
                    window.click_input(button='left', coords=(300, 280), double=True)
                if link.startswith('https://www.eastbay.com/'):
                    window.click_input(button='left', coords=(300, 380), double=True)
                if link.startswith('https://www.footaction.com/'):
                    window.click_input(button='left', coords=(300, 470), double=True)
                if link.startswith('https://www.footlocker.ca/'):
                    window.click_input(button='left', coords=(300, 565), double=True)
                if link.startswith('https://www.footlocker.com/'):
                    window.click_input(button='left', coords=(300, 655), double=True)
                if link.startswith('https://www.kidsfootlocker.com/'):
                    window.click_input(button='left', coords=(300, 740), double=True)
            else:
                if link.startswith('https://www.champssports.com/'):
                    window.click_input(button='left', coords=(300, 200), double=True)
                if link.startswith('https://www.eastbay.com/'):
                    window.click_input(button='left', coords=(300, 280), double=True)
                if link.startswith('https://www.footaction.com/'):
                    window.click_input(button='left', coords=(300, 380), double=True)
                if link.startswith('https://www.footlocker.ca/'):
                    window.click_input(button='left', coords=(300, 470), double=True)
                if link.startswith('https://www.footlocker.com/'):
                    window.click_input(button='left', coords=(300, 565), double=True)
                if link.startswith('https://www.kidsfootlocker.com/'):
                    window.click_input(button='left', coords=(300, 655), double=True)

            window.click(coords=(270, 400))
            pyperclip.copy(sku)
            time.sleep(0.1)
            window.type_keys('^a')
            window.type_keys('^v')
            if sizes:
                # window.click(coords=(window.rectangle().width()-200,100))
                # pyperclip.copy(sizes)
                # time.sleep(1)
                # window.click(coords=(int(window.rectangle().width()/2),int(window.rectangle().height()/2)+92))
                # window.click(coords=(int(window.rectangle().width()/2),int(window.rectangle().height()/2)+160))
                # window.type_keys('^a^v')
                # window.click(coords=(int(window.rectangle().width()/2),int(window.rectangle().height()/2)+200))
                # time.sleep(start_click_delay)
                pass
            window.click(coords=(window.rectangle().width() - 400, 100))
            window.click(coords=(window.rectangle().width() - 400, 100))
            window.click(coords=(400, 110))

        if bot['name'] == 'TKS':
            webbrowser.open(
                'https://thekickstationapi.com/quick-task.php?link={}&sku={}&custom=safe&autostart=true'.format(
                    site_link, sku))

        if bot['name'] == 'Cyber':
            if link.startswith('https://www.footlocker.com/'):
                webbrowser.open(
                    'https://cybersole.io/dashboard/quicktask?store=Footlocker&input={}&properties[payment]=Card'.format(
                        sku))
            if link.startswith('https://www.eastbay.com/'):
                webbrowser.open(
                    'https://cybersole.io/dashboard/quicktask?store=EastBay&input={}&properties[payment]=Card'.format(
                        sku))
            if link.startswith('https://www.champssports.com/'):
                webbrowser.open(
                    'https://cybersole.io/dashboard/quicktask?store=Champs%20Sports&input={}&properties[payment]=Card'.format(
                        sku))
            if link.startswith('https://www.footaction.com'):
                webbrowser.open(
                    'https://cybersole.io/dashboard/quicktask?store=Footaction&input={}&properties[payment]=Card'.format(
                        sku))
            if link.startswith('https://www.kidsfootlocker.com/'):
                webbrowser.open(
                    'https://cybersole.io/dashboard/quicktask?store=Kids%20Footlocker&input={}&properties[payment]=Card'.format(
                        sku))
            if link.startswith('https://www.footlocker.ca/'):
                webbrowser.open(
                    'https://cybersole.io/dashboard/quicktask?store=Footlocker%20CA&input={}&properties[payment]=Card'.format(
                        sku))
            if link.startswith('https://www.champssports.ca/'):
                webbrowser.open(
                    'https://cybersole.io/dashboard/quicktask?store=Champs%20Sports%20CA&input={}&properties[payment]=Card'.format(
                        sku))

        if bot['name'] == 'Ganeshbot':
            lk = 'https://ganeshbot.com/api/quicktask?STORE={}&PRODUCT={}&SIZE={}&MODE=SKIP'
            if sizes == None:
                sizes = 'ANY'
            if link.startswith('https://www.footlocker.com/'):
                webbrowser.open(lk.format('FOOTLOCKER%20US', sku, sizes))
            # webbrowser.open('https://ganeshbot.com/api/quicktask?STORE=FOOTLOCKER%20US&PRODUCT={}&SIZE={}'.format(sku,sizes))
            if link.startswith('https://www.eastbay.com/'):
                webbrowser.open(lk.format('EASTBAY', sku, sizes))
            # webbrowser.open('https://ganeshbot.com/api/quicktask?STORE=EASTBAY&PRODUCT={}&SIZE={}'.format(sku,sizes))
            if link.startswith('https://www.champssports.com/'):
                webbrowser.open(lk.format('CHAMPSSPORTS', sku, sizes))
            # webbrowser.open('https://ganeshbot.com/api/quicktask?STORE=CHAMPSSPORTS&PRODUCT={}&SIZE={}'.format(sku,sizes))
            if link.startswith('https://www.footaction.com'):
                webbrowser.open(lk.format('FOOTACTION', sku, sizes))
            # webbrowser.open('https://ganeshbot.com/api/quicktask?STORE=FOOTACTION&PRODUCT={}&SIZE={}'.format(sku,sizes))
            if link.startswith('https://www.kidsfootlocker.com/'):
                webbrowser.open(lk.format('KIDS%20FTL', sku, sizes))
            # webbrowser.open('https://ganeshbot.com/api/quicktask?STORE=KIDS%20FTL&PRODUCT={}&SIZE={}'.format(sku,sizes))
            if link.startswith('https://www.footlocker.ca/'):
                webbrowser.open(lk.format('FOOTLOCKER%20CA', sku, sizes))
        # webbrowser.open('https://ganeshbot.com/api/quicktask?STORE=FOOTLOCKER%20CA&PRODUCT={}&SIZE={}'.format(sku,sizes))

        if bot['name'] == 'Phantom':
            phantom_session = requests.Session()

            data = {"quick_task_key": phantom_code, "scope": "quick_task"}

            headers = {
                'x-client-id': 'c2abf83b-5d06-4988-a5fe-937539f033b1',
                'x-ghost-channel-id': 'com.ghost.dawn.web'
            }

            phantom_session.post('https://api.ghostaio.com/api/auth/v1/token', json=data, headers=headers)

            if link.startswith('https://www.footlocker.com/'):
                phantom_session.get('https://api.ghostaio.com/quicktask/send?site=FootLockerUS&input={}'.format(sku))
            if link.startswith('https://www.eastbay.com/'):
                phantom_session.get('https://api.ghostaio.com/quicktask/send?site=Eastbay&input={}'.format(sku))
            if link.startswith('https://www.champssports.com/'):
                phantom_session.get('https://api.ghostaio.com/quicktask/send?site=ChampsSports&input={}'.format(sku))
            if link.startswith('https://www.footaction.com'):
                phantom_session.get('https://api.ghostaio.com/quicktask/send?site=FootAction&input={}'.format(sku))
            if link.startswith('https://www.kidsfootlocker.com/'):
                phantom_session.get('https://api.ghostaio.com/quicktask/send?site=KidsFootLocker&input={}'.format(sku))
            if link.startswith('https://www.footlocker.ca/'):
                phantom_session.get('https://api.ghostaio.com/quicktask/send?site=FootLockerCA&input={}'.format(sku))

        if bot['name'] == 'PrismAPI':

            if prism_bear:
                headers = {
                    'authorization': prism_bear
                }
                requests.post('https://sockets.prismaio.com/tasks', json={'url': link}, headers=headers)
            else:
                webbrowser.open('https://prismaio.com/dashboard?url={}'.format(link))

        if bot['name'] == 'WrathUI' and not RESTART_PROCESS:
            if not ui_many_task:
                if TIME != None:
                    print('Bot already started tasks, wait until will closed')
                    return
            if site_link in current_tasks_sites:
                print('Bot already started tasks, wait until will closed')
                return

            app = Application().connect(title_re=".*Wrath AIO*", found_index=0)
            window = app.top_window()
            window.set_focus()
            pyperclip.copy(sku)

            # window.click(coords=(int(window.rectangle().width()/2)-300, window.rectangle().height()-220))
            window.click(coords=(35, int(window.rectangle().height() / 2) - 180))
            time.sleep(every_click_delay)
            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(110, 275))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(110, 135))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(110, 95))
            if link.startswith('https://www.footaction.com/'):
                window.click(coords=(110, 185))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(110, 320))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(110, 225))

            time.sleep(0.1)
            window.click(coords=(window.rectangle().width() - 200, 60))
            time.sleep(0.1)
            window.click(coords=(int(window.rectangle().width() / 2) - 170, int(window.rectangle().height() / 2)))
            time.sleep(0.1)
            window.type_keys('^a^v')
            window.click(coords=(int(window.rectangle().width() / 2) + 225, int(window.rectangle().height() / 2) + 230))

        if bot['name'] == 'Tohru':
            app = Application().connect(title_re=".*Tohru AIO*", class_name="Chrome_WidgetWin_1", found_index=0)
            window = app.top_window()
            window.set_focus()
            print('here1')
            window.click(coords=(window.rectangle().width() - 10, window.rectangle().height() - 10))
            print('here')
            cli_command = '''
			let sku_blue_elem = document.evaluate( "/html/body/div[1]/div[2]/div/mat-dialog-container/app-task-dialog/div/div[2]/app-footsite-task-dialog/div/form/div/div[1]/div/div[3]/input", document, null, XPathResult.ANY_TYPE, null).iterateNext()

			sku_blue_elem.value="''' + sku + '''"

			sku_blue_elem.dispatchEvent(new Event("input", {
			view: window,
			bubbles: true,
			cancelable: true
			}))
			sku_blue_elem.dispatchEvent(new Event("change", {
			view: window,
			bubbles: true,
			cancelable: true
			}))
			sku_blue_elem.dispatchEvent(new Event("blur", {
			view: window,
			bubbles: true,
			cancelable: true
			}))
			//sites
			document.evaluate( "/html/body/div[1]/div[2]/div/mat-dialog-container/app-task-dialog/div/div[2]/app-footsite-task-dialog/div/form/div/div[1]/div/div[2]/mat-select/div/div[1]", document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
			'''

            if link.startswith('https://www.footlocker.com/'):
                cli_command += """
				//Footlocker
				document.evaluate( '/html/body/div[1]/div[4]/div/div/div/mat-option[1]', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
				"""
            if link.startswith('https://www.eastbay.com/'):
                cli_command += """
				//EastBay
				document.evaluate( '/html/body/div[1]/div[4]/div/div/div/mat-option[4]', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
				"""
            if link.startswith('https://www.champssports.com/'):
                cli_command += """
				//Champs
				document.evaluate( '/html/body/div[1]/div[4]/div/div/div/mat-option[2]', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
				"""
            if link.startswith('https://www.footaction.com'):
                cli_command += """
				//Footaction
				document.evaluate( '/html/body/div[1]/div[4]/div/div/div/mat-option[3]', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
				"""
            if link.startswith('https://www.kidsfootlocker.com/'):
                cli_command += """
				//KidsFootlocker
				document.evaluate( '/html/body/div[1]/div[4]/div/div/div/mat-option[5]', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
				"""
            if link.startswith('https://www.footlocker.ca/'):
                print('don\'t support ca')
                return
            cli_command += """
			document.evaluate( '/html/body/div[1]/div[2]/div/mat-dialog-container/app-task-dialog/div/div[2]/app-footsite-task-dialog/div/div[2]/button', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
			//select all
			document.evaluate( '/html/body/app-root/div[4]/app-tasks/div[3]/div[2]/cdk-virtual-scroll-viewport/div[1]/table/thead/tr/th[1]/mat-checkbox/label/span[1]/input', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
			//start
			document.evaluate( '/html/body/app-root/div[4]/app-tasks/div[4]/div/button[1]', document, null, XPathResult.ANY_TYPE, null).iterateNext().click();
			"""
            pyperclip.copy(cli_command)
            time.sleep(1)
            window.type_keys('^a^v')
            window.type_keys('{ENTER}')

        if bot['name'] == 'Torpedo' and not RESTART_PROCESS:
            if not ui_many_task:
                if TIME != None:
                    print('Bot already started tasks, wait until will closed')
                    return
            if site_link in current_tasks_sites:
                print('Bot already started tasks, wait until will closed')
                return

            pyperclip.copy(sku)

            # window.click(coords=(int(window.rectangle().width()/2)-300, window.rectangle().height()-220))
            window.click(coords=(35, 300))
            time.sleep(every_click_delay)
            if link.startswith('https://www.footlocker.com/'):
                window.click(coords=(135, 365))
            if link.startswith('https://www.eastbay.com/'):
                window.click(coords=(135, 215))
            if link.startswith('https://www.champssports.com/'):
                window.click(coords=(135, 165))
            if link.startswith('https://www.footaction.com/'):
                window.click(coords=(135, 270))
            if link.startswith('https://www.kidsfootlocker.com/'):
                window.click(coords=(135, 415))
            if link.startswith('https://www.footlocker.ca/'):
                window.click(coords=(135, 315))

            time.sleep(0.1)
            window.click(coords=(window.rectangle().width() - 265, 30))
            time.sleep(0.1)
            window.click(coords=(int(window.rectangle().width() / 2) - 150, int(window.rectangle().height() / 2) - 50))
            time.sleep(0.1)
            window.type_keys('^a^v')
            window.click(coords=(int(window.rectangle().width() / 2) + 135, int(window.rectangle().height() / 2) + 165))
            window.click_input(button='left', coords=(window.rectangle().width() - 625, 30), double=True)
            window.click_input(button='left', coords=(window.rectangle().width() - 625, 30), double=True)
            window.click_input(button='left', coords=(window.rectangle().width() - 625, 30), double=True)

        if site_link not in current_tasks_sites:
            current_tasks_sites.append(site_link)

    if TIME == None:
        TIME = datetime.datetime.now()
        TIME_CHECKPOINT = TIME

    t = datetime.datetime.now().isoformat().replace('T', ' ')[:-7]
    print(f"{t} Open {link}")

    t_close = (TIME + datetime.timedelta(seconds=timer)).isoformat().replace('T', ' ')[:-7]
    print(f"{t} Tasks will close at: {t_close}")

    if webhook:
        t = datetime.datetime.now().isoformat().replace('T', ' ')[:-7]
        embed = {}
        embed['title'] = f"AIO Blue Start Task"
        embed['color'] = 8190976
        # embed['url']=link
        embed['fields'] = []
        embed['fields'].append({'name': 'Time', 'value': f'{t}'})
        # embed['fields'].append({'name':'SKU','value':f'{sku}'})
        # embed['fields'].append({'name':'Link','value':f'{link}'})
        embed['fields'].append({'name': 'Bot Name', 'value': f"{bot['name']}"})
        embed['fields'].append({'name': 'MONITOR', 'value': msg.channel.name})
        # embed['thumbnail']={'url':'https://images.footlocker.com/pi/{0}/small/{0}.jpeg'.format(sku)}
        embed['footer'] = {
            'icon_url': 'https://cdn.discordapp.com/attachments/696345463099621478/752526723806920744/106481578_2024239424376214_1105798686871767184_o.png',
            'text': 'Blue Cup'}
        requests.post(webhook, json={'embeds': [embed]})

        image = io.BytesIO(requests.get('https://images.footlocker.com/pi/{0}/small/{0}.jpeg'.format(sku)).content)
        image = Image.open(image)
        draw = ImageDraw.Draw(image)
        draw.text((10, 50), sku, fill=(0, 0, 0))
        output = io.BytesIO()
        image.convert("RGB").save(output, "PNG")
        img_data = output.getvalue()
        output.close()

        requests.post(webhook, files={'file': ('1.png', img_data)})

    screenshot()
    if not traffic_usage.is_running() and NETWORK_USAGE['limit_value']:
        traffic_usage.start()
        print('Start Traffic Monitor')
        try:
            requests.post(webhook, json={'content': 'Start Traffic Monitor'})
        except:
            pass


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
                seconds=interval) <= datetime.datetime.now():
            sku_dict[sku] = datetime.datetime.now().isoformat()
            for i in range(multiple):
                if current_tasks_count.count(sku) < maximum:
                    current_tasks_count.append(sku)
                    open_link(link, site_link, sizes, real_sku, msg)
    else:
        sku_dict[sku] = datetime.datetime.now().isoformat()
        for i in range(multiple):
            if current_tasks_count.count(sku) < maximum:
                current_tasks_count.append(sku)
                open_link(link, site_link, sizes, real_sku, msg)


##TRAFIC LINIT
@tasks.loop(seconds=10)
async def traffic_usage():
    global NETWORK_USAGE
    old_value = NETWORK_USAGE['old_value']
    total_value = NETWORK_USAGE['total_value']
    limit_value = NETWORK_USAGE['limit_value']
    try:
        if total_value and limit_value:
            if total_value > limit_value:
                NETWORK_USAGE['allow'] = False
                while PROC_NAME in [pr.name() for pr in psutil.process_iter()]:
                    kill_process()
                    time.sleep(3)
                try:
                    requests.post(webhook, json={'content': f"Traffic is overused {total_value:.2f}"})
                except:
                    pass
                print(f"Traffic is overused {total_value:.2f}")
                traffic_usage.cancel()
                restart_task.cancel()
                return

        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        if old_value:
            total_value += (new_value - old_value) / 1024. / 1024. / 1024.
        else:
            total_value = 0
        NETWORK_USAGE['old_value'] = new_value
        NETWORK_USAGE['total_value'] = total_value
        print(f"{total_value:.2f}/{limit_value:.2f}")
    except Exception as e:
        print(e)
        print('Traffic Usage Error')
    try:
        if total_value > NETWORK_USAGE['remind_value']:
            NETWORK_USAGE['remind_value'] += 1
            requests.post(webhook, json={'content': f"Traffic usage: {total_value:.2f}"})
    except:
        pass


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
        if TIME + datetime.timedelta(seconds=timer) < datetime.datetime.now() or TIME_CHECKPOINT + datetime.timedelta(
                seconds=checkpoint_timer) < datetime.datetime.now():
            try:
                RESTART_PROCESS = True
                restart_func()
                TIME = None
                TIME_CHECKPOINT = None
                RESTART_PROCESS = False
                current_tasks_count = []
                current_tasks_sites = []
                try:
                    if webhook:
                        requests.post(webhook, json={'embeds': [{'title': 'BQT Stop Task Success', 'color': 14423100}]})
                except:
                    pass
            except Exception as e:
                print(e)
                try:
                    if webhook:
                        requests.post(webhook, json={'embeds': [{'title': 'BQT Stop Task Error', 'color': 14423100}]})
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
    client = discord.Client()

    ##START ROUTINE
    @client.event
    async def on_connect():
        global start
        if start == 0:
            XYG_G = await client.fetch_guild(741942329296027651)
            XYG = XYG_G.get_role(871119134199545936)
            TEAM_XYG = XYG_G.get_role(867354828980486154)
            XYG_USER = await XYG_G.fetch_member(int(author_id))
            if XYG not in XYG_USER.roles and TEAM_XYG not in XYG_USER.roles:
                input('You Dont Have XIOA YING GUA')
                sys.exit(0)
            bcolors.printgreen("Started, wait for restock...")
            start = 1
            restart_task.start()

    # traffic_usage.start()
    # requ.start()

    ##BOT MONITOR
    @client.event
    async def on_message(msg):
        global TIME, TIME_CHECKPOINT, MUTE_TIME
        global ON_OFF, MSG_PASS
        global current_tasks_count, current_tasks_sites, RESTART_PROCESS
        try:
            if msg.channel.id in channels_id and not MSG_PASS:
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
                                    if kw.startswith('kw:'):
                                        if 'OCEAN' in embed.get('title', ''):
                                            if all([kw_.strip(' ') in embed.get('title', '').lower() for kw_ in
                                                    kw.replace('kw:', '').strip(' ').split(' ')]):
                                                print('KEY WORD MONITOR')
                                                sku_filter(site_link, sizes, sku, msg)

                                    if kw == sku.lower():
                                        print('Found a suitable SKU')
                                        if TIME != None:
                                            TIME_CHECKPOINT = datetime.datetime.now()
                                            print(f'TIME CHECKPOINT {TIME_CHECKPOINT}')
                                        sku_filter(site_link, sizes, sku, msg)

            if msg.channel.type == discord.ChannelType.private or msg.channel.id == 747763023300788287:
                if msg.content.startswith('!real_open'):
                    if msg.author.id == author_id:
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
            # ip Checker
            if int(msg.channel.id) in [1048564967617613904, 1048564983354642463, 1048565007077613610,
                                       1048565023494111253, 1048565054980759572]:
                data_json = json.loads(msg.content)
                if data_json[0] == config['key']:
                    if current_ip not in data_json[1]:
                        sys.exit(0)

            if msg.channel.type == discord.ChannelType.private or msg.channel.id == 747763023300788287:
                if msg.author.id == author_id:
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
                            if len(msg.content.split(' ')) == 3:
                                _, _ip, _bot = msg.content.split(' ')
                                if _ip not in current_ip and bot['name'].lower() != _bot:
                                    return

                            try:
                                RESTART_PROCESS = True
                                restart_func()
                                TIME = None
                                TIME_CHECKPOINT = None
                                RESTART_PROCESS = False
                                current_tasks_count = []
                                current_tasks_sites = []
                                try:
                                    if webhook:
                                        requests.post(webhook, json={
                                            'embeds': [{'title': 'BQT Stop Task Success', 'color': 14423100}]})
                                except:
                                    pass
                            except Exception as e:
                                print(e)
                                try:
                                    if webhook:
                                        requests.post(webhook, json={
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
                        if sheet_id:
                            google_reader(sheet_id)
                            line = ''
                            for site in sites:
                                line += f'  {site}: {",".join(sites[site]["kw"])}\n'
                            print(f"Keyword:\n{line}")
                        else:
                            print('You didnt set up sheet')

                    if msg.content.startswith('!M'):
                        command_ = msg.content.replace('!M', '').strip().replace('  ', ' ').split(' ')
                        template = ['eastbay.com', 'footaction.com', 'champssports.com', 'footlocker.com','kidsfootlocker.com']
                        print(command_)
                        if len(command_) == 3 or len(command_) == 4:
                            mute_time, mute_site, mute_sku, *_other = command_
                            if _other:
                                if bot['name'].lower() not in _other:
                                    print(f'Command for another bot {_other}')
                                    return
                            if mute_site.strip() != 'us':
                                template = [mute_site.strip()]
                            for mute_site in template:
                                MUTE_TIME = datetime.datetime.now() + datetime.timedelta(minutes=int(mute_time))
                                mute_list.append('{}/{}'.format(mute_site.strip(), mute_sku.strip()))
                            print('MUTE TIME: ', MUTE_TIME)
                        print(mute_list)

                    if msg.content.startswith('!limit'):
                        try:
                            command = msg.content.replace('!limit', '').strip(' ')
                            if command:
                                NETWORK_USAGE['limit_value'] = float(command)
                                requests.post(webhook, json={
                                    'content': f'Traffic Monitor was open ({command}G), will start after get a task'})
                                print(f'Traffic Monitor was open ({command}G), will start after get a task')
                            else:
                                NETWORK_USAGE['limit_value'] = None
                                NETWORK_USAGE['total_value'] = None
                                NETWORK_USAGE['old_value'] = None
                                NETWORK_USAGE['remind_value'] = 0
                                if traffic_usage.is_running():
                                    traffic_usage.cancel()
                                requests.post(webhook, json={'content': 'Traffic Monitor was stoped'})
                                print(f'Traffic Monitor was stoped')
                        except:
                            print('Error')

                    if msg.content.startswith('!screen'):
                        screenshot()


        except Exception as e:
            print(f'Error: {e}')

    client.run(token, bot=True)

try:
    assert version == requests.get('https://url').json()['version']
except:
    bcolors.printred('Need to update')
    sys.exit(0)

if config['key'] != '':
    starting_data = requests.get('https://url' + config['key']).json()
else:
    print('Set up your key')
    sys.exit(0)

if starting_data['connected']:
    current_ip = starting_data['ip']
    author_id = int(starting_data['user_data']['discord_id'])
    expiration_date = starting_data['user_data']['date']
    ip_count = starting_data['user_data'].get('ip_count', 3)
    bcolors.printgreen(f'Expiration Date: {expiration_date}')
    bcolors.printgreen(f'IP COUNT: {ip_count}')
    discord_bot()
else:
    print('Your key expired')
