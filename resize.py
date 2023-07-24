from PIL import Image

# Загружаем изображение
with open("logo/wsup.jpg", "rb") as image_file:
    image = Image.open(image_file)
    image = image.resize((60, 60))
    image.save("logo/wsup.jpg")