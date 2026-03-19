# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch >= 'A' and ch <= 'Z':
        result += chr(ord(ch) + 32)
    elif ch >= 'a' and ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)