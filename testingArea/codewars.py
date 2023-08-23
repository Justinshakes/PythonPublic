def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    if exam > 75 and projects >= 5:
        return 90
    if exam > 50 and projects >= 2:
        return 75
    return 0


def main():
    result1 = final_grade(100, 12)  # 100
    result2 = final_grade(85, 5)
    print(result1)
    print(result2)


main()
