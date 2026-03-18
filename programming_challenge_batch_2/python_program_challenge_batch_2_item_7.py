# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

even_counter = 0
for i in range(10):
    num = int(input(f"Enter a number {i + 1}: "))
    if num % 2 == 0:
        even_counter += 1
print("The number of even numbers entered is:", even_counter)