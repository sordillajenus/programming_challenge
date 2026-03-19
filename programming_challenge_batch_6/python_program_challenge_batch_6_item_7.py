# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
text = input("Enter a string: ")
width = int(input("Enter total width: "))

total_spaces = width - len(text)

if total_spaces <= 0:
    print(text)
else:
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    result = (" " * left_spaces) + text + (" " * right_spaces)
    print(result)