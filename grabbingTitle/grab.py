


import requests
import re
import sys

def parse(url):
    r = requests.get(url).text
    title = re.findall(r'<title>(.*?)</title>',r)
    return title


def main():
    result = parse(sys.argv[1])
    if result:
       print ('title page: ',result[0]))
       return
    return "title halaman mungkin gada"

if __name__=="__main__":
   main()
