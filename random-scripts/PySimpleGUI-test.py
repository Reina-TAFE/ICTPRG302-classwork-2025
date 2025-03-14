import random
import PySimpleGUI as sg
from texttable import Texttable

user_table = Texttable()

def shuffle_letters(unshuffled):
    shuffled = unshuffled
    random.shuffle(shuffled)
    return shuffled

def get_encrypted_alphabet():
    alphabet = []
    encrypted_alphabet = []
    for position in list(range(0, 26)):
        alphabet.append(chr(ord('a') + position))
        encrypted_alphabet.append(chr(ord('a') + position))
    encrypted_alphabet = shuffle_letters(encrypted_alphabet)
    print(alphabet)
    print(encrypted_alphabet)
    substitution_cipher = dict(zip(alphabet, encrypted_alphabet))
    substitution_cipher[" "] = " "
    print(substitution_cipher)
    return substitution_cipher

def make_table(user_dict):
    keys = [letter for letter in list(user_dict.keys())]
    keys.sort()
    values = [user_dict[key] for key in keys]
    user_table.reset()
    user_table.add_rows([keys[1:14], values[1:14]], False)
    user_table.add_row(([" "] * 13))
    user_table.add_rows([keys[14:27], values[14:27]], False)
    print(user_table)
    print(type(user_table))
    return

def play():
    cipher_dict = get_encrypted_alphabet()
    make_table(cipher_dict)

play()