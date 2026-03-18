# Prog08: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
print("Odd numbers from 0 to 100 are displayed below:")
numbers = 0
while numbers < 100:
    numbers += 1
    if numbers % 2 != 0:
        print(numbers)