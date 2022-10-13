import sys

print("Kuis Indonesia")

main = input("Mau main? ")
score = 0
if main.lower() != "mau":
    quit()

print("yeyy sini yuk kita main!\n")

soal = input("siapa presiden indonesia? ")
if soal.lower() == "jokowi":
    print("adalah benar")
    score += 1
else:
    print("salah coek")
    score -= 1

soal = input("logo partai terkuat di indonesia? ")
if soal.lower() == "banteng":
    print("adalah benar")
    score += 1
else:
    print("salah coek")
    score -= 1

soal = input("presiden tercantik di indonesia adalah? ")
if soal.lower() == "mega chan":
    print("adalah benar")
    score += 1
else:
    print("salah coek, yang bener itu mega chan ><")
    score -= 1

soal = input("singkatan dari kominfo adalah? ")
if soal.lower() == "kementrian komunikasi dan informatika":
    print("adalah benar")
    score += 1
else:
    print("salah coek")
    score -= 1

soal = input("harga ayam geprek? ")
if soal.lower() == "10k":
    print("adalah benar")
    score += 1
else:
    print("salah coek")
    score -= 1

if score >= 3:
    print("wahh kamu pinter juga yah, kamu mendapatkan nilai " + str(score*25))
else:
    print("geblek soal ginian aja gabisa ngerjain cuih")












sys.exit()
