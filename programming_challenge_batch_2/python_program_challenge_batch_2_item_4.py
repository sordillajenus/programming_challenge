# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num2 != 0:
    quotient = num1 // num2
    print("The quotient of the two numbers is:", quotient)
else:
    print("Error: Division by zero is not allowed.")