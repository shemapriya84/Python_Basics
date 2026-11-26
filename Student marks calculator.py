name = input("Enter student name: ")

tamil = int(input("Enter Tamil marks: "))
english = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))

total = tamil + english + maths
average = total / 3

print("Name:", name)
print("Total:", total)
print("Average:", average)

if tamil >= 50 and english >= 50 and maths >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")