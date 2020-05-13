from PIL import Image , ImageChops

img1 = Image.open("/Users/aashishsaini/Desktop/left.jpg")
img2  = Image.open("/Users/aashishsaini/Desktop/right.jpg")

diff = ImageChops.difference(img1,img2)
if diff.getbbox():
    diff.show()

