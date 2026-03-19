# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
text = input("Enter a string: ")

has_letter = False
all_upper = True

for ch in text:
    if ch >= 'a' and ch <= 'z':
        all_upper = False
    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        has_letter = True

if has_letter and all_upper:
    print(True)
else:
    print(False)