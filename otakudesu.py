import requests as req
import os
import pyshorteners
from bs4 import BeautifulSoup as bs

url = "https://otakudesu.video/"


def logo():
    os.system("clear")
    print("""    
  ____  __       __           __               
 / __ \/ /____ _/ /____ _____/ /__ ___ __ __   
/ /_/ / __/ _ `/  '_/ // / _  / -_|_-</ // /   
\____/\__/\_,_/_/\_\\\_,_/\_,_/\__/___/\_,_/     
                       Otakudesu GD Grabber
    """)


def search_anime():
    judul = input("[?] Judul Anime : ")
    open_url = bs(
        req.get(url+"?s={}&post_type=anime".format(judul)).content, "lxml")

    for anime in open_url.find_all("li", {"style": "list-style:none;"}):
        judul = anime.find("h2").find("a").get_text()
        info_anime = [stat.text.split(
            ":") for stat in anime.find_all("div", {"class": "set"})]
        link = anime.find("h2").find("a").get("href")

        print("\n[?] {}".format(judul))
        print("[•] Genres :{}".format(info_anime[0][1]))
        print("[•] Status :{}".format(info_anime[1][1]))
        print("[•] Rating :{}".format(info_anime[2][1]))
        print("\n[!] Link Download:")

        get_link(link)


def get_link(link):
    open_link = bs(req.get(link).content, "lxml")
    batch = open_link.find("a", {"rel": "follow"}).get("href")

    get_batch(batch)


def get_batch(link):
    open_batch = bs(req.get(link).content, "lxml")
    link_batch = []
    kualitas = []

    for data in open_batch.find_all("a"):
        if data.text == "OtakuDrive":
            link_batch.append(data.get("href"))

    for item in open_batch.find_all("strong"):
        kualitas.append(item.text)

    shortlink(link_batch, kualitas)


def shortlink(batch, kualitas):
    s = pyshorteners.Shortener()
    results = []

    for link in batch:
        results.append(s.tinyurl.short(link))

    i = 0
    while i < len(results):
        for result in results:
            print("[•] {} -> {}".format(kualitas[i], result))
            i += 1
    print("-"*40)


logo()
search_anime()
