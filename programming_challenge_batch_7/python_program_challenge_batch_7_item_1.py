# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
text = input("Enter a string with spaces at the end: ")

index = len(text) - 1

while index >= 0 and text[index] == " ":
    index -= 1

print(text[:index + 1])