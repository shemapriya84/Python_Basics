def check_number(n):

    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter number: "))

print(check_number(number))