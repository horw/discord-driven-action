import subprocess

prpr = subprocess.Popen(r"D:\Projects\Python\discord-driven-action\mock\dist\fly-mock.exe",
                                creationflags=subprocess.CREATE_NEW_CONSOLE,
                                stdin=subprocess.PIPE)

input()