from PIL import Image
    
portret = Image.open('images/gandalf.jpeg')
print(portret.size)
portret.show()

crop_area = (70, 0, 270, 200)
cropped_image = portret.crop(crop_area)
print(cropped_image.size)

thumbnail_size = (128, 130)
cropped_image.thumbnail(thumbnail_size)
print(cropped_image.size)

black_white = cropped_image.convert('L')
black_white.show()

logo = Image.open('images/VU.png')
thumbnail_size = (50, 50)
logo.thumbnail(thumbnail_size)
print(logo.size)

portret.paste(logo, (270, 5), logo)
portret.save('images/vugandalf.jpeg')










