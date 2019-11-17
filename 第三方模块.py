# 导入第三方模块
from PIL import Image,ImageFilter

im = Image.open(r"E:\水滴.jpg")
im2 = im.filter(ImageFilter.BLUR)
im2.save("E:\水滴2.jpg")

print("ok")