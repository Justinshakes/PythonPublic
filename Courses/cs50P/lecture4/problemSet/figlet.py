import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
    font_name = sys.argv[2]
else:
    sys.exit("Invalid usage")

figlet = Figlet(font=font_name)

text = input("Enter the text: ")
print(figlet.renderText(text))
