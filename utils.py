import io

import requests


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


def google_reader(sites, url):
    import csv
    bcolors.printblue("Downloading", url)
    response = requests.get(url)
    csv_data = io.StringIO(response.text)
    csv_reader = csv.reader(csv_data, delimiter=' ', quotechar='|')
    order = []
    for row in csv_reader:
        for el in row:
            if el.strip() == 'Champs Sport':
                pass

    sites['Champs Sport'] = {'link': 'https://www.champssports.com/', 'kw': fts_dict_[0]}
    sites['Eastbay'] = {'link': 'https://www.eastbay.com/', 'kw': fts_dict_[1]}
    sites['Footaction'] = {'link': 'https://www.footaction.com/', 'kw': fts_dict_[2]}
    sites['Footlocker'] = {'link': 'https://www.footlocker.com/', 'kw': fts_dict_[3]}
    sites['Footlocker'] = {'link': 'https://www.kidsfootlocker.com/', 'kw': fts_dict_[4]}
    # sites['Footlocker CA'] = {'link': 'https://www.footlocker.ca/', 'kw': fts_dict_[5]}
