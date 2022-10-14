from random import randint


def user(i):
    if i.lower() == "batu":
        return batu
    elif i.lower() == "gunting":
        return gunting
    elif i.lower() == "kertas":
        return kertas


def computer(i):
    if i.lower() == "batu":
        return batu
    elif i.lower() == "gunting":
        return gunting
    elif i.lower() == "kertas":
        return kertas


batu = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

gunting = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

kertas = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

data = ["batu", "gunting", "kertas"]
random = randint(0, 2)
comp = data[random]
print("~ Selamat Datang Dipermainan ~")
i = input("Masukkan Pilihan Anda (batu/gunting/kertas) : ")

if i.lower() in data:
    print(f"Pilihan Anda \n{user(i)}")
    print(f"Pilihan Computer \n{computer(comp)}")
else:
    print("Pilih hanya (batu/gunting/kertas)")

if i != comp:
    if i == "batu" and comp == "gunting":
        print("Kamu Menang !")
    elif i == "batu" and comp == "kertas":
        print("Kamu Kalah !")
    elif i == "gunting" and comp == "kertas":
        print("Kamu Menang !")
    elif i == "gunting" and comp == "batu":
        print("Kamu Kalah !")
    elif i == "kertas" and comp == "batu":
        print("Kamu Menang !")
    elif i == "kertas" and comp == "gunting":
        print("Kamu Kalah !")
else:
    print("Seri cuy !")
