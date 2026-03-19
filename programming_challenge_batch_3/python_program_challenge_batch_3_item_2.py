# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("Numbers entered (if duplicates are present, only the first entry will be displayed):")

displayed = []

for num in numbers:
    if num not in displayed:
        print(num)
        displayed.append(num)