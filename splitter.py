from PIL import Image, ImageOps
import sys

img = Image.open(sys.argv[1])

if len(sys.argv) > 2:
  border_px = int(sys.argv[2])
else:
  border_px = 100

color = "white"

width, height = img.size

left_box = (0, 0, width / 2, height)
left_img  = img.crop(left_box)
left_border = (border_px, border_px, 0, border_px)
left_img = ImageOps.expand(left_img, border=left_border, fill=color)
left_img_width, left_img_height = left_img.size
target_square = left_img_width if left_img_width > left_img_height else left_img_height
left_img = ImageOps.pad(left_img, (target_square, target_square), color=color, centering=(1,1))


right_box = (width / 2, 0, width, height)
right_img = img.crop(right_box)
right_border = (0, border_px, border_px, border_px)
right_img = ImageOps.expand(right_img, border=right_border, fill=color)
right_img = ImageOps.pad(right_img, (target_square, target_square), color=color, centering=(0,0))

file_name = sys.argv[1].replace(".jpg", "")

left_img.save(file_name + "_left.jpg")
right_img.save(file_name + "_right.jpg")
