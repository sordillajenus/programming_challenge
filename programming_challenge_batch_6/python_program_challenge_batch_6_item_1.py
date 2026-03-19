# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
text = input("Enter a string with spaces at the beginning: ")

index = 0

while index < len(text) and text[index] == " ":
    index += 1

print(text[index:])