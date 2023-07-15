
from PIL import Image

shirt_path = "shirt.png"
photo_path = "tester.jpg"

shirt = Image.open(shirt_path)
photo = Image.open(photo_path)

print(shirt.size)
print(photo.size)

# Resize the photo image to the desired dimensions
resized_photo = photo.resize(photo.size)

width, height = resized_photo.size

# Resize the shirt image to match the size of the photo
resized_shirt = shirt.resize(photo.size)

# Paste the resized shirt image onto the photo
resized_photo.paste(resized_shirt, (0, 0), mask=resized_shirt)

resized_photo.show()  # Display the resulting image with the pasted shirt










# path = "Justin.txt"
#
# root, ext = os.path.splitext(path)
# print(ext)
