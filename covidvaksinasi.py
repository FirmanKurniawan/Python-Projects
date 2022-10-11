import requests
import json

# API by : 
# https://covid19.mathdro.id/api/
# https://cekdiri.id/vaksinasi/

def vaksin():
	url = requests.get("https://cekdiri.id/vaksinasi/", headers={'User-Agent': 'Mozilla/5.0'}).text
	data = json.loads(url)

	for vksn in data['monitoring']:
		print("\nTanggal Vaksinasi => ", vksn['date'])
		print("Jumlah  Vaksinasi 1 => {:,}".format(vksn['vaksinasi1']))
		print("Jumlah  Vaksinasi 2 => {:,}".format(vksn['vaksinasi2'],'\n'))

def world():
	url = requests.get("https://covid19.mathdro.id/api/").text
	data = json.loads(url)

	print("\nJumlah Terkonfirmasi => {:,}".format(data['confirmed']['value']))
	print("Jumlah Yang Sembuh => {:,}".format(data['recovered']['value']))
	print("Jumlah Yang Meninggal => {:,}".format(data['deaths']['value']))

def banner():

	print("""

 $$$$$$\   $$$$$$\  $$\    $$\ $$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$ |   $$ |\_$$  _|$$  __$$\ 
$$ /  \__|$$ /  $$ |$$ |   $$ |  $$ |  $$ |  $$ |
$$ |      $$ |  $$ |\$$\  $$  |  $$ |  $$ |  $$ |
$$ |      $$ |  $$ | \$$\$$  /   $$ |  $$ |  $$ |
$$ |  $$\ $$ |  $$ |  \$$$  /    $$ |  $$ |  $$ |
\$$$$$$  | $$$$$$  |   \$  /   $$$$$$\ $$$$$$$  |
 \______/  \______/     \_/    \______|\_______/     


     		  https://cekdiri.id/vaksinasi/                               
		""")

	opsi = print("1. Jumlah Vaksinasi di Indonesia")
	opsi = print("2. Jumlah Covid di Seluruh Dunia","\n")

	choose = input('Choose => ')
	if choose == '1':
		vaksin()
	elif choose == '2':
		world()
	else:
		print('Pilihan Tidak Tersedia')

#End
if __name__ == "__main__":
	banner()
