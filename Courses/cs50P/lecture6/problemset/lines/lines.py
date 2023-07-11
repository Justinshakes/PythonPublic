import sys

if len(sys.argv) != 2 or not sys.argv[1].endswith(".py"):
    sys.exit("Invalid argument, must be a single .py file")

with open(sys.argv[1]) as file:
    lines = file.readlines()

code_line_count = 0

for line in lines:
    if '#' not in line and line.strip() != '':
        code_line_count += 1
        print(line, end="")

print(code_line_count)
