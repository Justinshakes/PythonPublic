def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    if age < 18:
        return "drink coke"
    if age < 21:
        return "drink beer"
    else:
        return "drink whisky"

def main():
    # Test cases
    result1 = people_with_age_drink(13)
    result2 = people_with_age_drink(17)
    result3 = people_with_age_drink(18)
    result4 = people_with_age_drink(20)
    result5 = people_with_age_drink(30)

    # Print results
    print(result1)  # Expected: "drink toddy"
    print(result2)  # Expected: "drink coke"
    print(result3)  # Expected: "drink beer"
    print(result4)  # Expected: "drink beer"
    print(result5)  # Expected: "drink whisky"

main()
