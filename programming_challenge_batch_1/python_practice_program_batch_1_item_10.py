# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
print("Numbers from 0 to 100 except numbers ending in zero are listed below:")
for number in range(0, 101):
    if number % 10 != 0:
        print(number)   