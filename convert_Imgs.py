from PIL import Image 
2 import sys 
3 import os 
4 
 
5 try: 
6   im = None 
7   for root, dirs, files in os.walk("."): 
8     for filename in files: 
9         if filename.endswith('.jpg'): 
10           im = Image.open(filename).convert("RGB") 
11           im.save(filename.replace('jpg', 'png'), "png") 
12         elif filename.endswith('.png'): 
13           im = Image.open(filename).convert("RGB") 
14           im.save(filename.replace('png', 'jpg'), "jpeg") 
15         else: 
16           print('dont have image to convert') 
17 except IOError: 
18   print('directory empty!') 
19   sys.exit() 
