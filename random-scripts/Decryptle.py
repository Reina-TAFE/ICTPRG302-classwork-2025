# Decryptle (Decryption Game)
#
# Short Test script to demonstrate arithmetic, logical, and unary operators
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-28
#
import random as rnd

TARGET_WORDS_LIST = open('./word-bank/target_words.txt')
TARGET_WORDS = (TARGET_WORDS_LIST.read()).split()
TARGET_WORDS_LIST.close()


def encrypt(unencrypted_word, cypher_index):
    output = ""
    for character in unencrypted_word:
        if character.isalpha():
            cypher_letter = ord(character) + cypher_index
            if cypher_letter > ord('z'):
                cypher_letter = ord('a') + (cypher_letter % 26)
            elif cypher_letter < ord('a'):
                cypher_letter = ord('z') - (cypher_letter % 26)
            output += chr(cypher_letter)

        else:
            output += character

    return output

def get_random_hints(number_of_hints):
    hint_words = [None] * number_of_hints
    for i in range(0, number_of_hints):
        hint = rnd.choice(TARGET_WORDS).lower()
        if hint not in hint_words:
            hint_words[i] = hint
        else:
            i -= 1
    return hint_words

def get_encrypted_hints():
    difficulty = int(input("How many hints would you like?: "))
    cypher_key = rnd.randrange(1, 26)
    hints = dict.fromkeys(get_random_hints(difficulty))
    for word in hints.keys():
        hints[word] = encrypt(word, cypher_key)
    cypher = [cypher_key, hints]
    return cypher

def play():
    encrypted_cypher = get_encrypted_hints()
    while True:
        print(list({x + 1: chr((ord("a")+x)) for x in range(0, 26)}.items()))
        print()
        for hint in list(encrypted_cypher[1].values()):
            print(hint)
        guess_key = int(input("What is the cypher key?"))
        if guess_key == encrypted_cypher[0]:
            for decrypted_word in encrypted_cypher[1].keys():
                print(f"{decrypted_word} : {encrypt(encrypted_cypher[1][decrypted_word], (0 - guess_key))}")
            print("Correct!! You Win!")
            input()
            quit()
        elif guess_key == 500: # debug code
            print(f"key = {encrypted_cypher[0]}")
            for answer in list(encrypted_cypher[1].items()):
                print(answer)
        else:
            for guess_decryption in list(encrypted_cypher[1].values()):
                print(encrypt(guess_decryption, (0 - guess_key)))
            print("incorrect cypher key. Try again")

play()