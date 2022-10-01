import base64

various = """
        1.Encrpyt 
        3.Decrpyt
"""
print(various)
pil = int(input("Pilih: "))
if pil == 1:
  mastr = input("input sebuah teks: ").encode("ascii")
  basee = base64.b64encode(mastr)
  b = basee.decode("ascii")
  print(b)
  print(type(b))
  
if pil == 3:
  mast = input("input hash base64: ").encode("ascii")
  based = base64.b64decode(mast).decode("ascii")
  #b = based.decode("ascii")
  print(based)
  print(type(based))
