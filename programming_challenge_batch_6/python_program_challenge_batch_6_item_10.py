# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
text = input("Enter a string: ")
result = ""
new_word = True

for ch in text:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            if ch >= 'a' and ch <= 'z':
                result += chr(ord(ch) - 32)
            else:
                result += ch
            new_word = False
        else:
            if ch >= 'A' and ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch

print(result)