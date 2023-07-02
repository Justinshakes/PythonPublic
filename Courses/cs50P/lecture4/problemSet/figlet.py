import sys
from pyfiglet import Figlet

# Create an instance of the Figlet class
figlet = Figlet()

# Check if the command-line arguments are valid
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
    # If the arguments are valid, store the font name
    font_name = sys.argv[2]
else:
    # If the arguments are invalid, exit the program with an error message
    sys.exit("Invalid usage")

# Create a new instance of the Figlet class with the specified font
figlet = Figlet(font=font_name)

# Prompt the user to enter a text
text = input("Enter the text: ")

# Render the text using the chosen font and print it
print(figlet.renderText(text))
