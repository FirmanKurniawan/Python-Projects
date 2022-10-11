#!/usr/bin/env python3

import requests
import json
import argparse

def SendgridCheck(apikey):
    try:
        url = 'https://api.sendgrid.com/v3/user/credits'
        headers = {"authorization": "Bearer "+ apikey }
        getInfo = requests.get(url, headers=headers)
        limit = json.loads(getInfo.text)['total']
        used = json.loads(getInfo.text)['used']
        reset = json.loads(getInfo.text)['reset_frequency']
        print(f"Limit    : {limit}")
        print(f"Used     : {used}")
        print(f"Reset    : {reset}")
        with open("results.txt", "a") as x:
            x.write(f"APIKEY: {apikey}\nLimit: {limit}\nUsed: {used}\nReset: {reset}\n\n")
        print('------------------------------------------------')
    except:
        print('Error    :', json.loads(getInfo.text)['errors'][0]['message'])
        print('------------------------------------------------')

parser = argparse.ArgumentParser()
parser.add_argument('-s', metavar='YOURAPIKEY', help='Single check')
parser.add_argument('-f', metavar='FILE', help='Multiple check use lists in file')
args = parser.parse_args()

print("""
 __                _            _     _   ___ _               _             
/ _\ ___ _ __   __| | __ _ _ __(_) __| | / __\ |__   ___  ___| | _____ _ __ 
\ \ / _ \ '_ \ / _` |/ _` | '__| |/ _` |/ /  | '_ \ / _ \/ __| |/ / _ \ '__|
_\ \  __/ | | | (_| | (_| | |  | | (_| / /___| | | |  __/ (__|   <  __/ |   
\__/\___|_| |_|\__,_|\__, |_|  |_|\__,_\____/|_| |_|\___|\___|_|\_\___|_|   
                     |___/                                                  
----------------------------------------------------------------Tegal1337
""")

if args.s and args.f:
    print('[ERROR] Please use single argument')
    exit()
elif args.s:
    print('[APIKEY] '+ args.s)
    SendgridCheck(args.s)
elif args.f:
    try:
        with open(args.f, "r") as f:
            for apikey in f.readlines():
                print('[APIKEY] '+ apikey.strip())
                SendgridCheck(apikey.strip())
    except:
        print('[ERROR] File not found')
else:
    parser.print_help()