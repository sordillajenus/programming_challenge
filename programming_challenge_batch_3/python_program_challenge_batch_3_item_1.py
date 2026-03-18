# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate
numbers = []

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

print("Numbers that don't have duplicates:")
for num in numbers:
    if numbers.count(num) == 1:
        print(num)