# Caesar Cipher With functions
#
# Author:   Adrian Gould
# Date:     2025-02-28

# welcome function:
#     display program introduction message
#     obtain user name
#     welcome message with user name
#     return user name

def welcome():
    print("Welcome to the Caesar Cipher app")
    name = input("What is your name? ")
    print(name, ", hope you enjoy encrypting...")
    return (name)


# encrypt function:
#     parameters: letter and shift
#     determine encrypted character
#     return encrypted character

def encrypt(letter, shift):
    if letter.isalpha():
        answer = chr(ord(letter) + shift)
    else:
        answer = letter
    return (answer)


# main program:
# call welcome function
welcome()
# ask user for letter and shift
letter = input("Letter to encrypt: ")

try:
    shift = int(input("Number of Characters to Shift: "))
except():
    # if shift cannot be converted to an integer: display error message,
    print("ERROR: Integer number needed for shift")
    # encrypted character = letter
    encrypted_character = letter
    shift = 0
# else call encrypt function
else:
    encrypted_character = encrypt(letter, shift)

# display encrypted character
print(letter, " when shifted by ", shift, " is ", encrypted_character)
