# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
text = input("Enter a string: ")
width = int(input("Enter total width: "))

result = text

while len(result) < width:
    result += " "

print(result)