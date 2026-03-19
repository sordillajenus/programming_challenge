# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if len(numbers) == 0:
    print("No numbers were entered")
else:
    max_count = 0
    most_duplicate_number = numbers[0]

    for num in numbers:
        count = numbers.count(num)
        if count > max_count:
            max_count = count
            most_duplicate_number = num

    print("The number with the most duplicates is:", most_duplicate_number)
    print("It appears", max_count, "times")