# Caesar Cypher
#
# Author:   Adrian Gould
# Date:     2025-02-14

print("Welcome to Caesar Cypher program")

name = input("What is your name? ")
print(name + ", hope you enjoy encrypting and decrypting words")

letter = input("Enter a letter to encrypt:")
shift = input("Number of characters to shift: ")

try:
    shift = int(shift)
except: # this is a BARE/NAKED except, it is not best practice
    end_of_program = input("Invalid shift, press any key to exit")
    quit()

if letter.isalpha():
    ord_value = ord(letter)
    ord_value = ord_value + shift
    answer = chr(ord_value)
    print("Caesar cypher letter is:", answer)
else:
    print("You entered a non alpha character.")
