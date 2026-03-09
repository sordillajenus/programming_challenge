# Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
if first_number > second_number:
    print(f"The bigger number is: {first_number}")
elif second_number > first_number:
    print(f"The bigger number is: {second_number}")
else:
    print("Both numbers are equal. Please enter different numbers.")