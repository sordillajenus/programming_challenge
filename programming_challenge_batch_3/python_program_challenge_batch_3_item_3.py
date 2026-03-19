# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))

        if num in numbers:
            print("Duplicate: Counted as invalid input. Ending program.")
            break
        else:
            print("Unique")

        numbers.append(num)

    except ValueError:
        break