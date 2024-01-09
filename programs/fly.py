import os
import subprocess
import time

import psutil

from programs.base import ProgramBase


class Fly(ProgramBase):
    name = 'Fly'
    path = ''
    tasks_path = ''
    proc_name = 'fly-cli.exe'

    def __init__(self, path):
        self.fly_windows = []
        self.path = path
        self.tasks_path = self.path.replace('fly-cli.exe', '') + 'tasks.csv'
        self.DATA = b''
        self.DATA_CA = b''

    def start(self, link, sku, sizes=None):
        os.remove(self.tasks_path)
        if sizes is None:
            sizes = 'random'
        if '.ca/' in link:
            open(self.tasks_path, 'wb+').write(
                self.DATA_CA.decode('utf-8').replace('SITEBQT', link.replace('https://www.', '').split('/')[0]).replace(
                    'SIZEBQT', sizes).replace('SKUBQT', sku).encode('utf-8'))
        else:
            open(self.tasks_path, 'wb+').write(
                self.DATA.decode('utf-8').replace('SITEBQT', link.replace('https://www.', '').split('/')[0]).replace(
                    'SIZEBQT', sizes).replace('SKUBQT', sku).encode('utf-8'))

        os.chdir(self.path.replace('fly-cli.exe', ''))
        print("Start program on path: ", self.path)
        prpr = subprocess.Popen(f"{self.path}",
                                creationflags=subprocess.CREATE_NEW_CONSOLE,
                                stdin=subprocess.PIPE)
        self.fly_windows.append(prpr)
        try:
            prpr.stdin.write(b'\n')
            prpr.stdin.flush()
        except:
            print("Command send to fly")

    def restart(self):
        while self.fly_windows:
            process = psutil.Process(self.fly_windows.pop().pid)
            process.terminate()

        nf = True
        while nf:
            nf = False

            for proc in psutil.process_iter():
                if self.proc_name == proc.name():
                    try:
                        exe_path = proc.exe()
                    except Exception as e:
                        print(e)
                        continue

                    if self.path in exe_path:
                        nf = True
                        try:
                            proc.kill()
                        except Exception as e:
                            continue
            time.sleep(3)

        print('Process was killed')
