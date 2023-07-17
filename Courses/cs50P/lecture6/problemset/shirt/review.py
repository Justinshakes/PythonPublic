import os
import sys
from PIL import Image, ImageOps


def main():
    check_command_line()

    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt_file = Image.open("shirt.png")
    size = shirt_file.size

    muppet = ImageOps.fit(image_file, size)

    muppet.paste(shirt_file, shirt_file)

    muppet.save(sys.argv[2])


def check_command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file_type1 = os.path.splitext(sys.argv[1])
    file_type2 = os.path.splitext(sys.argv[2])

    if not check_extension(file_type1[1]):
        sys.exit("Invalid input")
    if not check_extension(file_type2[1]):
        sys.exit("Invalid output")

    if file_type1[1].lower() != file_type2[1].lower():
        sys.exit("Input and output have different extensions")


def check_extension(file):
    valid_extensions = [".jpg", ".jpeg", ".png"]
    return file.lower() in valid_extensions
