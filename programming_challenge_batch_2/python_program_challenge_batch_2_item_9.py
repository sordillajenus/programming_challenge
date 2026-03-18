# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
print("Numbers from 0 to 100 except numbers ending in zero or ending five are displayed below:")    
numbers_not_ending_in_zero_and_five = 0 
while numbers_not_ending_in_zero_and_five < 100: 
    numbers_not_ending_in_zero_and_five += 1 
    if numbers_not_ending_in_zero_and_five % 5 != 0:
     print(numbers_not_ending_in_zero_and_five)