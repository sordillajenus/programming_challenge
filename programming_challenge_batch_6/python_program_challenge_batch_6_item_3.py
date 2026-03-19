# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
text = input("Enter a string: ")
result = ""

for ch in text:
    if ch >= 'A' and ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)