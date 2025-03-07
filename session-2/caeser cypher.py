# Operators Test
#
# Short Test script to demonstrate arithmetic, logical, and unary operators
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-14
#

# word = input("please enter your word: ")
cypher_index = input("please enter the cypher key: ")


try:
    cypher_index = int(cypher_index)
except ValueError:
    input("Invalid cypher index. press enter to stop")
    quit()

def encrypt(word):
    output = ""
    for character in word:
        if character.isalpha():
            cypher_letter = ord(character) + cypher_index
            if cypher_letter > ord('z'):
                cypher_letter = ord('a') + (cypher_letter % 26)
            output += chr(cypher_letter)

        else:
            output += character

    return output
