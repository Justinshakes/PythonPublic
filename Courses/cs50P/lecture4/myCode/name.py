import sys

# Check for errors in command line arguments
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print(arg)
