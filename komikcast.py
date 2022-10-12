# toolgabut

import requests as req
import os
from bs4 import BeautifulSoup as bs

url = "https://komikcast.net/"


def logo_search():
    print("""
 _   __                _ _                 _   
| | / /               (_) |               | |  
| |/ /  ___  _ __ ___  _| | _____ __ _ ___| |_ 
|    \ / _ \| '_ ` _ \| | |/ / __/ _` / __| __|
| |\  \ (_) | | | | | | |   < (_| (_| \__ \ |_ 
\_| \_/\___/|_| |_| |_|_|_|\_\___\__,_|___/\__|

        Komik Information Scraper
            from KomikCast ID
    """)


def search(query, num=0, tempLink=[]):
    # site = f"{url}?s={query}"
    # request = req.get(site)
    # soup = bs(request.content, "lxml")
    # contoh lebih simple dri yg diatas :3
    cek = bs(req.get(url+"?s={}".format(query)).content, "lxml")

    mangas = cek.find(class_="film-list")
    animepost = mangas.find_all("div", {"class": "animepost"})
    for komik in animepost:
        num += 1
        judul = komik.find("div", {"class": "tt"}).get_text().strip()
        rating = komik.find("div", {"class": "rating"}).find("i").get_text()
        links = komik.find("a")
        tempLink.append(links.get("href"))
        jenis = ""

        if komik.find("span", {"class": "typeflag Manhwa"}):
            jenis = "Manhwa"
        elif komik.find("span", {"class": "typeflag Manga"}):
            jenis = "Manga"
        elif komik.find("span", {"class": "typeflag Manhua"}):
            jenis = "Manhua"

        print(f"\n{num}. {judul}")
        print(f"   • Jenis : {jenis}")
        print(f"   • Rating : {rating}")

    if len(tempLink) == 0:
        return False
    else:
        return tempLink


def info_komik(link):
    cek = bs(req.get(link).content, "lxml")

    title = cek.find(class_="entry-title").get_text()
    chapter = [last.text.split("Chapter ")
               for last in cek.find_all(class_="barunew")]
    genres = [genre.text for genre in cek.find(
        class_="genre-info").find_all("a")]
    sinopsis = cek.find(class_="entry-content entry-content-single").get_text()
    sub_info = [sub.text for sub in cek.find(class_="spe").find_all("span")]

    print(f"\n[•] {title}\n")
    print(f"Status\t: {sub_info[1].split()[1]}")
    print(f"Jenis\t: {sub_info[2].split()[2]}")
    print("Author\t: {}".format("".join(sub_info[3].split()[1:])))
    print(f"Rilis\t: {sub_info[5].split()[1]}")
    print("Genre\t: {}".format(", ".join(genres)))
    print(f"Chapter\t: {chapter[1][1]}")
    print(f"\nSinopsis:{sinopsis}")
    print(f"Link Website:\n{link}")


def main_menu():
    os.system("clear")
    logo_search()
    query = input("Judul : ")
    if query == "":
        exit("Masukin Judul Bre -_-")
    cari = search(query)
    if cari == False:
        print("Komik yang anda cari tidak ada..")
    else:
        print("")
        pilih = input("Pilih : ")
        while int(pilih) == 0 or int(pilih) > len(cari):
            print("\nPilih yang bener bre")
            pilih = input("Pilih : ")

        scan = cari[int(pilih)-1]
        info_komik(scan)


main_menu()
