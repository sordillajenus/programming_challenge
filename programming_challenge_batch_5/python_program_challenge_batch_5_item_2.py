# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
number = input("Enter a number from 0 to 1000: ")
print(number.zfill(6))