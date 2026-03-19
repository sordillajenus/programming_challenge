# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
text = input("Enter a string: ")
target = input("Enter the characters to find: ")

found = False

for i in range(len(text) - len(target) + 1):
    if text[i:i + len(target)] == target:
        print(i)
        found = True
        break

if not found:
    print("Substring not found")