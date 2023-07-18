import re

email = input("What's your email? ").strip()
# \w means word            \ escape charcter
if re.search(r'^\w+@(\w+\.)?\w+\.edu$', email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
