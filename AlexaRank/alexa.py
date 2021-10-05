import requests
import re
import os
requests.packages.urllib3.disable_warnings()


def stats():

	url = input('Input your website -> ')
	r = requests.get('https://data.alexa.com/data?cli=10&dat=snbamz&url={}'.format(url), verify=False)
	alexa = re.findall('TEXT="(.*)" SOURCE="panel"', r.text)

	if 'SOURCE="panel"' in r.text:
		print(30 * '=')
		print('[+]', url)
		for a in alexa:
			print('[+] Alexa Rank :', a)
		print(30 * '=')
	else:
		print(30 * '=')
		print('[+]', url)
		print('[-] Not Ranked!')


def mass():

	url = input('Input list of website -> ')
	yaa = open(url, 'r').readlines()
	for i in yaa:
		boo = i.strip()
		r = requests.get('https://data.alexa.com/data?cli=10&dat=snbamz&url={}'.format(boo), verify=False)
		alexa = re.findall('TEXT="(.*)" SOURCE="panel"', r.text)

		if 'SOURCE="panel"' in r.text:
			print(30 * '=')
			print('[+]', boo)
			for a in alexa:
				print('[+] Alexa Rank :', a)
			open('alexa.txt', 'a').write('Domain :'+boo+'\n'+'Alexa Rank :'+a+'\n'+'\n')
		else:
			print(30 * '=')
			print('[+]', boo)
			print('[-] Not Ranked!')

def banner():

	print("""

	Alexa Rank Checker CLI
	Single or Mass

	Created by Abdi Pranata / SinonX

		""")

if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print('[+] 1. Single Check')
	print('[+] 2. Mass Check')
	print('\n')

	pilih = input('Choose Option! ')

	if pilih == '1':
		stats()
	elif pilih == '2':
		mass()
	else:
		print('No Options!')