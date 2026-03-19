# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch >= 'a' and ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result += ch

print(result)