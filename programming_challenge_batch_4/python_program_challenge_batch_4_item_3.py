# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

numbers = []

while True:
    try:
        num = int(input("Enter your number: "))
        numbers.append(num)
    except ValueError:
        break
    
if len(numbers) > 0:
    print("The highest number is:", max(numbers))
else:
    print("No valid numbers were entered.")