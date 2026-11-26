marks = [78, 85, 90, 65, 88]

total = 0

for mark in marks:
    print(mark)
    total = total + mark

average = total / len(marks)

print("Total =", total)
print("Average =", average)
print("Highest =", max(marks))
print("Lowest =", min(marks))