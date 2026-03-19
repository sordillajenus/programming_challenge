# Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
fullname = input("Enter your fullname: ")
words = fullname.lower().split()
print("_".join(words))