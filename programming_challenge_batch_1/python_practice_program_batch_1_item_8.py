# Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

odd_counter = 0
for i in range(1, 11):
    number = int(input(f"Enter Number{i}: "))
    if number % 2 != 0:
        odd_counter += 1

print(f"There are {odd_counter} odd numbers.")