#coded by Putra 
#HacktoberFest2021
import requests, os, sys, re, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import base64
import random
import string
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
import urllib
from bs4 import BeautifulSoup

fr  =   Fore.RED
fh  =   Fore.RED
fc  =   Fore.CYAN
fo  =   Fore.MAGENTA
fw  =   Fore.WHITE
fy  =   Fore.YELLOW
fbl =   Fore.BLUE
fg  =   Fore.GREEN                                          
sd  =   Style.DIM
fb  =   Fore.RESET
sn  =   Style.NORMAL                                        
sb  =   Style.BRIGHT
bb = ('{}{}[').format(fbl,sb)+('{}{}+').format(fy,sb)+('{}{}]').format(fbl,sb)
"""
def grabber():
    gr = raw_input('\t        '+bb+('{}{} Give me List Servers: ').format(fr,sb))
    gr = open(gr,'r')
    for done in gr:
        remo = []
        page = 1
        while page < 251:
            bing = "http://www.bing.com/search?q=ip%3A"+done+"+&count=50&first="+str(page)
            opene = requests.get(bing,verify=False,headers=headers)
            read = opene.content
            findwebs = re.findall('<h2><a href="(.*?)"', read)
            for i in findwebs:
                o = i.split('/')
                if (o[0]+'//'+o[2]) in remo:
                    pass
                else:
                    remo.append(o[0]+'//'+o[2])
                    print '{}[XxX]'.format(fg,sb),(o[0]+'//'+o[2])
                    with open('Sites.txt','a') as s:
                        s.writelines((o[0]+'//'+o[2])+'\n')
            page = page+50
if __name__ == "__main__":
    grabber()"""
try:
    os.system('clear')
    ganteng = input('ur files => ')
    f= open(ganteng, 'r') 
    woh = f.read().splitlines()
except IOError:
    pass
woh = list((woh))

def Domains(url):

    if '://' not in url:
        return 'http://'+url
    else:
        return url

#
def grabber(site):
    url = Domains(site)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:57.0) Gecko/20100101 Firefox/57.0"}
    kontel = urlparse(url)
    anjinglo = kontel.netloc

    remo = []
    page = 1
    while page < 251:
        bing = "http://www.bing.com/search?q=ip%3A"+anjinglo+"+&count=50&first="+str(page)
        opene = requests.get(bing,verify=False,headers=headers)
        read = opene.content.decode('utf-8')
        findwebs = re.findall('<h2><a href="(.*?)"', read)
        for i in findwebs:
            o = i.split('/')
            if (o[0]+'//'+o[2]) in remo:
                pass
            else:
                print(anjinglo)
                remo.append(o[0]+'//'+o[2])
                print ('{}[XxX]'.format(fg,sb),(o[0]+'//'+o[2]))
                with open('Sites3.txt','a') as s:
                    s.writelines((o[0]+'//'+o[2])+'\n')
        page = page+50

def Run_Work(site):
    url = Domains(site)
    grabber(url)

def Main():


    start = timer()
    pp = ThreadPool(40)
    pr = pp.map(Run_Work, woh)
    print('Time: ' + str(timer() - start) + ' seconds')


if __name__ == "__main__":
    Main()