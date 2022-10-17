#python 3.10.4
class idulfitri():
    def maaf(self):
        self.maaf = "Selamat Hari Raya Idul Fitri\nMohon maaf lahir dan batin"
        print(self.maaf)
    def salah(self):
        self.salah = input("\ngw salah gak?: \nTrue/False\t> ")
        if self.salah == "True" or self.salah == "true":
            print("Bila ada kesalahan mohon dimaafkan")
        elif self.salah == "False" or self.salah == "false":
            print([
                "Kalian semua sudah kumaafkan",
                "btw menerima thr ","089xxxxxxx",
                "gopay, ovo, dana :v ditunggu gan "
            ])
if __name__ == "__main__":
    idulfitri().maaf()
    idulfitri().salah()
