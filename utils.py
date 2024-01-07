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
    bcolors.printblue(f"Downloading {url}")
    response = requests.get(url)
    csv_data = io.StringIO(response.text)
    csv_reader = csv.reader(csv_data, delimiter=',', quotechar='"')
    reserved_col = [-1] * 10
    for row in csv_reader:
        print(row)
        for ind, val in enumerate(row):
            if val.strip() == 'Champs Sport':
                reserved_col[0] = ind
            if val.strip() == 'Champs Sport Size':
                reserved_col[1] = ind

            if val.strip() == 'Eastbay':
                reserved_col[2] = ind
            if val.strip() == 'Eastbay Size':
                reserved_col[3] = ind

            if val.strip() == 'Footaction':
                reserved_col[4] = ind
            if val.strip() == 'Footaction Size':
                reserved_col[5] = ind

            if val.strip() == 'Footlocker':
                reserved_col[6] = ind
            if val.strip() == 'Footlocker Size':
                reserved_col[7] = ind

            if val.strip() == 'Kids Footlocker':
                reserved_col[8] = ind
            if val.strip() == 'Kids Footlocker Size':
                reserved_col[9] = ind
        if sum(reserved_col) != -10:
            break

    if sum(reserved_col) == -10:
        return
    prepare = [[] for _ in range(5)]
    for row in csv_reader:
        for ii in range(5):
            i = ii * 2
            if reserved_col[i] == -1 or row[reserved_col[i]].strip() == '':
                continue
            sku = row[reserved_col[i]]
            if reserved_col[i+1] != -1:
                size = row[reserved_col[i+1]]
                prepare[ii].append(f"{sku}SS:{size}")
            else:
                prepare[ii].append(sku)

    sites['Champs Sport'] = {'link': 'https://www.champssports.com/', 'kw': prepare[0]}
    sites['Eastbay'] = {'link': 'https://www.eastbay.com/', 'kw': prepare[1]}
    sites['Footaction'] = {'link': 'https://www.footaction.com/', 'kw': prepare[2]}
    sites['Footlocker'] = {'link': 'https://www.footlocker.com/', 'kw': prepare[3]}
    sites['Kids Footlocker'] = {'link': 'https://www.kidsfootlocker.com/', 'kw': prepare[4]}
