from PIL import Image, ImageFilter

im = Image.open('python.jpg')
print(im.format, im.size, im.mode)
print(im.getextrema())
print(im.getpixel((256, 256)))
new_im = im.convert('L').rotate(90).filter(ImageFilter.GaussianBlur())
new_im.show()
new_im.save('python2.jpg', quality=95)
