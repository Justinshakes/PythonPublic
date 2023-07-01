import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
else:
    print("Invalid number of arguments. Please provide one argument.")
