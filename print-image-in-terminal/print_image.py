# https://github.com/404rgr/print-image-in-terminal
import numpy
from PIL import Image

class print_image:
    def __init__(self, image_path):
       self.image_path = image_path
       self.main()
    def main(self):
       image = Image.open(self.image_path)
       height = 100
       width = int((image.width / image.height) * height)
       print(width)
       image = image.resize((width,height), Image.ANTIALIAS)
       image_array = numpy.asarray(image)
       height,width,c = image_array.shape
       print(height,width,c)

       for x in range(height):
           for y in range(width):
              px = image_array[x][y]
              print(self.get_color(px[0], px[1], px[2]), sep='', end='')
           print()
    def get_color(self, r, g, b):
       return "\x1b[48;5;{}m \x1b[0m".format(int(self.get_ansi_color_code(r,g,b)))
    def get_ansi_color_code(self, r, g, b):
       if r == g and g == b:
          if r < 8:
              return 16
          if r > 248:
              return 231
          return round(((r - 8) / 247) * 24) + 232
       return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


import sys
if len(sys.argv) > 1:
   try:
     print_image(sys.argv[1])
   except FileNotFoundError:
     print("File Not Found")
else:
   print('display the image in the terminal in python')
   print('Source Code: https://github.com/404rgr/display-image-in-terminal')
   print()
   print('Example: python3 print_image.py shinchan.jpg')
