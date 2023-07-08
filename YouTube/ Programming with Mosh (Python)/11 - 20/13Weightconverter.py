
weight = float(input("Weight: "))
kg_lb = input("(L)bs or (K)g: ").lower()
if kg_lb == "k":
    weight = round(weight * 2.205, 1)
    print(f"You are {weight} Pounds")
elif kg_lb == "l":
    weight = round(weight / 2.205, 1)
    print(f"You are {weight} Kilograms")
else:
    print("Invalid Input")



# weight_lbs = weight_kg * 2.205
#
# weight_kg = weight_lbs / 2.205,

