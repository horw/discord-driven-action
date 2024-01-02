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
