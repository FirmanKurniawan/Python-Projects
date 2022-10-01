import chess
import chess.engine
import chess.pgn
import random
import os
import re
import time
from configparser import ConfigParser
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

#mode ada 3 pilihan yaitu : bullet, blitz, rapid. bullet untuk langkah cepat pertandingan 1 menit, blitz untuk pertandingan 3-5 menit, rapid untuk pertandingan 10 menit
mode = 'bullet'
pengguna = ''
#lokasi file
lokasi_file = os.path.abspath(__file__)
lokasi_engine = "/engine/stockfish.exe"
lokasi_stockfish = lokasi_file[:-9] + lokasi_engine
lokasi_akun = lokasi_file[:-8] + "akun.txt"
total_cari_lawan = 0
jika_menang = ""
#kredensial akun
def Kredensial():
    global pengguna
    with open(lokasi_akun, "r") as f:
        pengguna = f.readline().strip()
        kata_sandi = f.readline().strip()
    if not pengguna and not kata_sandi:
        print("Nama pengguna / kata sandi tidak tersedia di akun.txt")
        pengguna = input("username: ")
        kata_sandi = input("password: ")
    return [pengguna, kata_sandi]

#selenium
def buka_selenium():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0")
    gecko_loc = lokasi_file[:-8] + "geckodriver.exe"
    driver = webdriver.Firefox(profile, executable_path=gecko_loc)
    driver.get("https://www.chess.com/login")
    return driver

#masuk
def masuk(driver, pengguna, kata_sandi):
    form_pengguna = driver.find_element_by_id("username")
    form_pengguna.send_keys(pengguna)
    form_katasandi = driver.find_element_by_id("password")
    form_katasandi.send_keys(kata_sandi)
    form_katasandi.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.get("https://www.chess.com/live")  

#buat notasi / pgn
def buat_notasi():
    lokasi_notasi = lokasi_file[:-8]+"history/pgn.pgn"
    open(lokasi_notasi, "w+").close
    return lokasi_notasi

#deteksi langkah gerakan
def deteksi_gerakan(driver, letak_gerakan):
    warnanya = [1, 0]
    gerakan_selanjutnya = ""
    warna = warnanya[letak_gerakan%2]
    lokasi = (letak_gerakan+1)//2
    xpath = f"/html/body/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div[{lokasi}]/span[{warna+2}]/span[contains(@class, 'vertical-move-list-clickable')]"
    WebDriverWait(driver, 120).until(
    EC.presence_of_element_located((By.XPATH, xpath))
    )
    pindah = driver.find_element_by_xpath(xpath)
    print(letak_gerakan, pindah.text)

    if pindah.text[0].isdigit():
        print("GAME SELESAI")
        driver.get("https://www.chess.com/live")
        return
    if letak_gerakan % 2 == 1:
        return str(lokasi) + "." + pindah.text + " "
    else:
        return pindah.text + " "

#mencari langkah terbaik
def cari_terbaik(engine, notasi, depth):
    with open(notasi, "r") as f:
        game = chess.pgn.read_game(f)
        papan = chess.Board()
        for pindah in game.mainline_moves():
            papan.push(pindah)
        terbaik = engine.play(papan, chess.engine.Limit(depth=depth)).move
        return terbaik

#skip aborted game
def skip_aborted():
    try:
        sudah = driver.find_element_by_class_name("game-over-dialog-content")
        if sudah:
            try:
                time.sleep(5)
                permainan_baru = driver.find_element_by_class_name("game-over-button-button").click()
                print("Skip game yang dibatalkan")
                time.sleep(1)
                driver.get("https://www.chess.com/live")
            except:
                pass
    except:
        pass
    
    #jika lawan langung mengaku kalah / mengalah
    try:
        mengalah = driver.find_element_by_class_name("game-over-header-userWon")
        if mengalah:
            try:
                time.sleep(5)
                permainan_baru = driver.find_element_by_class_name("game-over-button-button").click()
                print("Skip game karena lawan mengalah")
                time.sleep(1)
                driver.get("https://www.chess.com/live")
            except:
                pass
    except:
        pass

    #jika akun gratisan akan muncul notif tidak bisa search macth 2x sekaligus
    # try:
    #     tantangan = driver.find_element_by_class_name("challenge-multiple-games-body")
    #     if tantangan:
    #         try:
    #             time.sleep(2)
    #             close = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[1]/div/div[2]/div[2]/button[1]").click()
    #             print("Skip tantangan karena akun tidak memumpuni")
    #         except:
    #             pass
    # except:
    #     pass


#pilih promosi pion yang sekolah
def ambil_promosi(driver, terbaik):
    #untuk bisa menggunakan fitur ini silahkan email : tinwaninja@gmail.com
    dapat_promosi = ['tinwaninja@gmail.com']
    try:
        if any(str(terbaik) in item for item in dapat_promosi):
            print("Promosi ditemukan ",terbaik)
    except:
        pass

#main game
def main_game(driver, engine, otomatis_main, depth, warna):
    global mode, jika_menang
    notasi = buat_notasi()
    time.sleep(1)
    try:
        if "win 0" not in jika_menang: 
            if warna == 'putih':
                warna_kotak(driver, 'e2e4')
                gerakan_otomatis(driver)

        for letak_gerakan in range(1,500):
            skip_aborted()
            if letak_gerakan == 1 or letak_gerakan == 2:
                if "win 0" in jika_menang: 
                    print("Lawan terlalu cupu, mencoba abort match dengan delay 25 detik")
                    jika_menang = ""
                    time.sleep(25)
                    return
            gerakan_selanjutnya = deteksi_gerakan(driver, letak_gerakan)
            with open(notasi, "a") as f:
               f.write(gerakan_selanjutnya)
            terbaik = cari_terbaik(engine, notasi, depth)
            if((warna == 'putih' and letak_gerakan % 2 == 0) or (warna == 'hitam' and letak_gerakan % 2 == 1)):
                if mode == 'bullet':
                    if letak_gerakan <= 15:
                        waktu = random.uniform(0.0,0.0)
                        print('delay', waktu,' detik')
                        time.sleep( waktu )
                    if letak_gerakan >= 15:
                        waktu = random.uniform(0.0,0.0)
                        print('delay', waktu,' detik')
                        time.sleep( waktu )
                if mode == 'blitz':
                    if letak_gerakan <= 15:
                        waktu = random.uniform(0.05,0.25)
                        print('delay', waktu,' detik')
                        time.sleep( waktu )
                    if letak_gerakan >= 15:
                        waktu = random.uniform(0.05,1.25)
                        print('delay', waktu,' detik')
                        time.sleep( waktu )
                if mode == 'rapid':
                    if letak_gerakan <= 15:
                        waktu = random.uniform(0.05,1.25)
                        print('delay', waktu,' detik')
                        time.sleep( waktu )
                    if letak_gerakan >= 15:
                        waktu = random.uniform(0.05,2.25)
                        print('delay', waktu,' detik')
                        time.sleep( waktu )
                warna_kotak(driver, terbaik)
                gerakan_otomatis(driver)
                ambil_promosi(driver, terbaik)
                
    except:
        return

#cari warna
def cari_warna(driver, otomatis_main):
    global total_cari_lawan, jika_menang
    while (1):
        try:
            if otomatis_main:
                try:
                    cek = driver.find_element_by_class_name("game-over-dialog-content")
                    print("Mengecek pertandingan apakah telah berakhir")
                    if cek:
                        try:
                            sudah = driver.find_element_by_class_name("game-over-button-seeking")
                            print("Menunggu lawan")
                        except:
                            time.sleep(2)
                            try:
                                rematch = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/button[2]").text
                                if rematch != 'Rematch':
                                    sebelumnya_kalah = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[1]/h3").text
                                    if "You Won" in sebelumnya_kalah: 
                                        if "win 0" not in jika_menang: 
                                            #ini untuk acc rematch yang pemain setara
                                            rematch = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/button[2]").click()
                                            print("Acc rematch karena pemain setara")
                                        else: 
                                            #ini untuk tolak rematch pemain cupu
                                            rematch = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/button[1]").click()
                                            print("Menolak rematch karena pemain cupu")
                                    else:
                                        rematch = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/button[1]").click()
                                        print("Menolak rematch karena pemain terlalu pro")
                            except:
                                time.sleep(2)
                                baru = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/button[1]").click()
                                if baru:
                                    print("Mencoba mencari pertandingan baru")
                            try:
                                permainan_baru = driver.find_element_by_class_name("game-over-button-button").click()
                                print("Mencoba mencari pertandingan baru")
                            except:
                                try:
                                    time.sleep(1)
                                    driver.find_element_by_xpath("//li[@data-tab='challenge']").click()
                                    driver.find_element_by_class_name("quick-challenge-play").click()
                                except:
                                    pass
                except:
                    try:
                        cek = driver.find_element_by_class_name("quick-challenge-play").click()
                        print("Membuat tantangan pertandingan baru")
                    except:
                        pass
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'draw-button-component')))
            break
        except TimeoutException:
            print("Menunggu pertandingan dimulai ",total_cari_lawan)
            total_cari_lawan += 1
            if(total_cari_lawan > 8):
                total_cari_lawan = 0
                try:
                    baru = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[4]/div[2]/div/div[4]/button[1]").click()
                    if baru:
                        print("Mencoba mencari pertandingan baru")
                except:
                    pass
                driver.get("https://www.chess.com/live")

    komponen = driver.find_elements_by_class_name("chat-message-component")
    try:
        if('warn-message-component' in komponen[-1].get_attribute('class')):
            warna_mentah = komponen[-2]
        else:
            warna_mentah = komponen[-1]
        jika_menang = warna_mentah.text
        print(warna_mentah.text)
    except:
        return
    warna_pengguna = re.findall(r'(\w+)\s\(\d+\)', warna_mentah.text)

    cek_putih = warna_pengguna[0]

    global pengguna
    global mode
    print('mode kecepatan permainan: ' + mode)
    if cek_putih == pengguna:
        print(pengguna + ' bermain sebagai putih')
        return "putih"
    else:
        print(pengguna + ' bermain sebagai hitam')
        return "hitam"

#suggest warna
def warna_kotak(driver, terbaik):
    kotak_awal = str(terbaik)[:2]
    kotak_tujuan = str(terbaik)[2:]
    lokasi_awal = str(0) + str(ord(kotak_awal[0])-96) + str(0) + kotak_awal[1]
    lokasi_tujuan = str(0) + str(ord(kotak_tujuan[0])-96) + str(0) + kotak_tujuan[1]
    driver.execute_script("""
    element = document.createElement('div');
    element.setAttribute("id", "highlight1");
    style1 = "background-color: rgb(255,0,0); opacity: 0.5;"
    class1 = "square square-{lokasi_awal} marked-square"
    element.setAttribute("style", style1)
    element.setAttribute("class", class1)
    document.getElementById("game-board").appendChild(element)
    element = document.createElement('div');
    element.setAttribute("id", "highlight2");
    style2 = "background-color: rgb(0,255,255); opacity: 0.5;"
    class2 = "square square-{lokasi_tujuan} marked-square"
    element.setAttribute("style", style2)
    element.setAttribute("class", class2)
    document.getElementById("game-board").appendChild(element)
    """.format(lokasi_awal = lokasi_awal, lokasi_tujuan = lokasi_tujuan))
    
#gerakan otomatis
def gerakan_otomatis(driver):
    element = driver.find_element(By.XPATH, '//*[@id="highlight1"]')
    ActionChains(driver).move_to_element_with_offset(element, 0, 2).click().perform()
    time.sleep(0.05)
    element = driver.find_element(By.XPATH, '//*[@id="highlight2"]')
    ActionChains(driver).move_to_element_with_offset(element, 0, 2).click().perform()
    return

#buat pengaturan 
def set_pengaturan():
    pengaturan = ConfigParser()
    pengaturan['DEFAULT'] = {'depth': '7',
                         'autoStart': '0'}
    with open('config.ini', 'w') as f:
        pengaturan.write(f)

#buka pengaturan
def buka_pengaturan():
    pengaturan = ConfigParser()
    pengaturan.read('config.ini')
    depth = int(pengaturan['DEFAULT']['depth'])
    otomatis_main = int(pengaturan['DEFAULT']['autoStart'])
    return depth, otomatis_main

#fungsi main
def main():
    driver = buka_selenium()
    pengguna, kata_sandi = Kredensial()
    masuk(driver, pengguna, kata_sandi)
    engine = chess.engine.SimpleEngine.popen_uci(lokasi_stockfish)
    main_lagi = 1
    depth, otomatis_main = buka_pengaturan()
    while main_lagi:
        skip_aborted()
        warna = cari_warna(driver, otomatis_main)
        main_game(driver, engine, otomatis_main, depth, warna)
        if otomatis_main:
            main_lagi = 1
        else:
            masukan = input("Ketik 'start' untuk lanjut suggest (ketika pertandingan sudah dimulai), atau ketik 'no' untuk keluar: ")
            if masukan == 'no':
                main_lagi = 0
    driver.close()
    engine.close()

if __name__ == "__main__":
    main()