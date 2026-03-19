# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
text = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")

if len(suffix) <= len(text) and text[len(text) - len(suffix):] == suffix:
    print(text[:len(text) - len(suffix)])
else:
    print(text)