"""
if temperature is greater than 30
    it's a hot day
otherwise if it's less than 10
    it's a cold day
otherwise it's neither hot nor cold
"""

# temperature = 30
#
# if temperature > 30:
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

name = "Justin"

if len(name) < 3:
    print("Name must be a least 3 characters")
elif len(name) > 50:
    print("Name can be maximum of 50 characters")
else:
    print("Name looks good!")
