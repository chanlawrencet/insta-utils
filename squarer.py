from PIL import Image, ImageOps
import sys

img = Image.open(sys.argv[1])

if len(sys.argv) > 2:
  border_px = int(sys.argv[2])
else:
  border_px = 100

color = "white"

width, height = img.size

border = (border_px, border_px, border_px, border_px)
img = ImageOps.expand(img, border=border, fill=color)

width, height = img.size
target_square = width if width > height else height


img = ImageOps.pad(img, (target_square, target_square), color=color, centering=(0.5,0.5))

file_name = sys.argv[1].replace(".jpg", "")

img.save(file_name + "_square.jpg")
