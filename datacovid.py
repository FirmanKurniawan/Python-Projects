#!/usr/bin/python

from requests import *
from json import *
from time import sleep
from tqdm import tqdm

banner = lambda : f'''
  _____        _                         _     _
 |  __ \      | |                       (_)   | |
 | |  | | __ _| |_ __ _    ___ _____   ___  __| |
 | |  | |/ _` | __/ _` |  / __/ _ \ \ / / |/ _` |
 | |__| | (_| | || (_| | | (_| (_) \ V /| | (_| |
 |_____/ \__,_|\__\__,_|  \___\___/ \_/ |_|\__,_| indonesia
                    CLI version
        my profile: https://github.com/gitcomeon8

'''
class main:

    def __init__(self):
        self.url = "https://api.kawalcorona.com/indonesia"
        self.get = get(self.url).text

    def parse(self):
        try:
            for i in tqdm(range(10)):
                sleep(0.2)
            self.js = loads(self.get)
            for x in self.js:
                for c in x:
                    print (f'[*] {c}: {x[c]}')
        except Exception as er:
            print (f'[!] {er}')


if __name__=='__main__':
    print (banner())
    main().parse()
