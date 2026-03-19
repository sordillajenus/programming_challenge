# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("The last input is invalid")
        break

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print("The average is:", average)
else:
    print("No valid numbers were entered.")