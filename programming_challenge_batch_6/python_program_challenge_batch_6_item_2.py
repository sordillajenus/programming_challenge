# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
text = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

if text[:len(prefix)] == prefix:
    print(text[len(prefix):])
else:
    print(text)