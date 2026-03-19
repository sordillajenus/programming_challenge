# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
text = input("Enter a string: ")
result = ""

for i in range(len(text)):
    ch = text[i]

    if i == 0 and ch >= 'a' and ch <= 'z':
        result += chr(ord(ch) - 32)
    elif i > 0 and ch >= 'A' and ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)