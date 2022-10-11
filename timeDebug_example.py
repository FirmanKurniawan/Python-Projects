import time
from time import sleep
from random import choice


def main():
   print("[simple program to display time for verbose mode]")
   print("hacktoberfest - 2022\n\n")
   out = "number on progress: "
   for _ in range(1,100):
      _ += 3.5 - 1 + choice([z for z in range(1,1000)]) + 0 + 1337
      print(time.strftime("[\033[92m%Y:%M:%T\033[97m]"),out,_);sleep(5)


if __name__=="__main__":
   main()
