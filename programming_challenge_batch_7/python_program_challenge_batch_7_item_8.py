# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
text = input("Enter a string: ")
target = input("Enter the characters to count: ")

count = 0
target_len = len(target)

for i in range(len(text) - target_len + 1):
    if text[i:i + target_len] == target:
        count += 1

print(count)