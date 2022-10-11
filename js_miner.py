import requests
from bs4 import BeautifulSoup
import sys


class Jsminer:
    url_main: str

    def __init__(self, url_main):
        self.url_main = url_main

    @staticmethod
    def banner():
        print("""
    _____                  __       __  __                               
   /     |                /  \     /  |/  |                              
   $$$$$ |  _______       $$  \   /$$ |$$/  _______    ______    ______  
      $$ | /       |      $$$  \ /$$$ |/  |/       \  /      \  /      \ 
 __   $$ |/$$$$$$$/       $$$$  /$$$$ |$$ |$$$$$$$  |/$$$$$$  |/$$$$$$  |
/  |  $$ |$$      \       $$ $$ $$/$$ |$$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
$$ \__$$ | $$$$$$  |      $$ |$$$/ $$ |$$ |$$ |  $$ |$$$$$$$$/ $$ |      
$$    $$/ /     $$/       $$ | $/  $$ |$$ |$$ |  $$ |$$       |$$ |      
 $$$$$$/  $$$$$$$/        $$/      $$/ $$/ $$/   $$/  $$$$$$$/ $$/       
                                                        v 1.0      

        """)

    def getting_js(self):
        response = requests.get(self.url_main)
        data = response.text
        js = []
        if data:
            soup = BeautifulSoup(data, 'html.parser')
            for script in soup.find_all('script'):
                js.append(script.get('src'))

        return js

    def test_js_url(self):
        js = self.getting_js()
        urls = []
        for url in js:
            if url:
                if url.startswith('http'):
                    urls.append(url)
                else:
                    urls.append(self.url_main + url)
        return urls

    def testing_urls(self):
        self.banner()
        urls = self.test_js_url()
        d = []
        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                d.append(url)
        return d


if __name__ == '__main__':
    if len(sys.argv) == 2:
        url_main = sys.argv[1]
        jsminer = Jsminer(url_main).testing_urls()
        for url in jsminer:
            print(url)
    else:
        print('Usage:js_miner <url>')
        sys.exit(1)
