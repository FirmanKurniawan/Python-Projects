#!/usr/bin/python
import os
import string
import random
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import requests
from time import time as timer
requests.packages.urllib3.disable_warnings()

def banner():
    print("Zekkel ganteng")
def scanner(webnya):
    if "://" not in webnya:
        target = "http://"+webnya
    else:
        target = webnya

    exploiter = "/wp-includes/"
    exploiter2 = "wp-content"

    try:
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0"}
        request = requests.get(target, verify=False, timeout=5, headers=headers).text
        if exploiter2 in request:
            print("{} -> WordPress" .format(target))
            open('result_wp.txt', 'a').write(target+"\n")
        elif exploiter in request:
            print("{} -> WordPress" .format(target))
            open('result_wp.txt', 'a').write(target+"\n")

        else:
            print("{} -> Unknown CMS" .format(target))
    except Exception as e:
        print("{} -> Unknown Error : {}" .format(target,e))
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    mmc = input(' LIST : ')
    threadny = input(' Thread : ')
    a = open(mmc, 'r').read().splitlines()
    
    ThreadPool = Pool(int(threadny))
    Threads = ThreadPool.map(scanner, a)

    #Hacktoberfest-indonesia-2021
    #Freedom133
