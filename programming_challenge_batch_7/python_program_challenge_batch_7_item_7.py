# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
text = input("Enter a number as string: ")
width = int(input("Enter total width: "))

result = text

while len(result) < width:
    result = "0" + result

print(result)