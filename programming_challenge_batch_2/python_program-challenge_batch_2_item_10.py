number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))

print("The numbers between", number_1, "and", number_2, "are displayed below:")

if number_1 < number_2:
    for i in range(number_1 + 1, number_2):
        print(i)
elif number_2 < number_1:
    for i in range(number_2 + 1, number_1):
        print(i)
else:
    print("The two numbers are equal, so there are no numbers between them.")