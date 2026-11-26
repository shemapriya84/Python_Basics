def get_grade(average):

    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"

print(get_grade(85))
print(get_grade(72))
print(get_grade(45))