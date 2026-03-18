# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
remainder = number_1 % number_2
print("The remainder when", number_1, "is divided by", number_2, "is:", remainder)