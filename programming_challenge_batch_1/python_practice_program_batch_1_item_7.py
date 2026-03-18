# Prog07: Create a program that asks the user to input 10 numbers and prints the sum of all the numbers.
total = 0

for i in range(1, 11):
    number = float(input(f"Enter number {i}: "))
    total += number

print(f"The sum of all the numbers is: {total}")