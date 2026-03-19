# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
text = input("Enter a string: ")

has_letter = False
all_lower = True

for ch in text:
    if ch >= 'A' and ch <= 'Z':
        all_lower = False
    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        has_letter = True

if has_letter and all_lower:
    print(True)
else:
    print(False)