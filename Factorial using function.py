def factorial(n):

    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

number = int(input("Enter number: "))

if number < 0:
    print("Enter a non-negative number")
else:
    print("Factorial =", factorial(number))