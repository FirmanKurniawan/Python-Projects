import time
dang = time.strftime('%H:%M:%S')



def banner():
	print("[+] Zekkel AR")
	print("[+] Remove Duplicate")


def remove():
	try:
		zong = input('Ur FILE => ')
		fileName = zong
	except:
		print('You didn\'t supply a valid filename.')
		exit()

	with open(fileName, 'r') as f:
		file = f.readlines()

	wordList = []
	badList = []

	for line in file:
		if line in wordList:
			badList.append(line)
		else:
			wordList.append(line)

	file = open(fileName, 'w')
	for line in wordList:
		file.write(line)
	file.close()
	print('[{0}]: {1} duplicate lines removed from {2}.'.format(dang, len(badList), fileName))


if __name__ == "__main__":
	banner()
	remove()