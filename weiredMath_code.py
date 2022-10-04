
import os
import sys
import random

try:
   from manages import filteringData
except:
   sys.exit("you must create manage folder and code fD for run!\nBye~~~ xD")

extends_files = list(filter(None,open(sys.argv[1],"r").read().split("\n")))
jsonResponse = json.loads(filteringData.manage().files)

def main():
   for _ in range(10):
      x,y,z,end = 1337,999,666,[z for z in range(1,2947291)]
      e = x + z - y + y * 1337 * 12 + random.choice(end)
      ee = 12*12 * x + 1982 * 17 - e + e * x + y - z + random.choice(end)
      uni,sov = str("0x00")+str(ee),"0x00"+str(e)
      payload = {"msg_":f'"ERROR:".$e->getMessage({uni})',"data":JsonResponse}
      for _ in range(10):
          print((f"{uni} ::: {sov} > {payload['msg_']} == {payload['data']}"))

if __name__=="__main__":
   main()

