from PIL import Image , ImageChops
import numpy as np
from skimage.metrics import structural_similarity
import cv2

high_res = Image.open("/Users/aashishsaini/PycharmProjects/k&k/data/K&N ROTO/Main Images/test/high_res.jpg")
low_res  = Image.open("/Users/aashishsaini/PycharmProjects/k&k/data/K&N ROTO/Main Images/test/low_res.jpg")

high_res_size = high_res.size
low_res_size = low_res.size

max_size = (min(high_res_size[0], low_res_size[0]), min(high_res_size[1], low_res_size[1]))

resized_high_res_image = high_res.resize(max_size)
resized_low_res_image = low_res.resize(max_size)

# resized_high_res_image.save("high.jpeg")
# resized_low_res_image.save("low.jpeg")
#
# img1 = cv2.imread("/Users/aashishsaini/PycharmProjects/k&k/scripts/high.jpeg")
# img2 = cv2.imread("/Users/aashishsaini/PycharmProjects/k&k/scripts/low.jpeg")


# diff = ImageChops.difference(resized_high_res_image, resized_low_res_image)
# if diff.getbbox():
#     diff.show()

# gray_high_res = cv2.cvtColor(np.float32(resized_high_res_image), cv2.COLOR_BGR2GRAY)
# gray_low_res = cv2.cvtColor(np.float32(resized_low_res_image), cv2.COLOR_BGR2GRAY)

img1 = cv2.imread("/Users/aashishsaini/PycharmProjects/k&k/target_img/B0075VEJVI.jpg")
img2 = cv2.imread("/Users/aashishsaini/PycharmProjects/k&k/target_img/B000CO81AK.jpg")

gray_high_res = cv2.cvtColor(np.float32(img1), cv2.COLOR_BGR2GRAY)
gray_low_res = cv2.cvtColor(np.float32(img2), cv2.COLOR_BGR2GRAY)

(score, diff) = structural_similarity(gray_high_res, gray_low_res, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))
