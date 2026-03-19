# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
fullname = input("Enter your fullname: ")
words = fullname.title().split()
print("".join(words))