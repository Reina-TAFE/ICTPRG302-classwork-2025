import random
import PySimpleGUI as sg
from texttable import Texttable

user_table = Texttable()
MESSAGE = "the quick brown fox jumps over the lazy dog"

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
    keys_layout = []
    values_layout = []
    for i in keys:
        keys_layout.append(sg.Text(i))
        keys_layout.append(sg.VerticalSeparator(color='red'))
    for j in values:
        values_layout.append(sg.Text(j))
        values_layout.append(sg.VerticalSeparator(color="red"))
    table_layout = [keys_layout, values_layout]
    return table_layout

def get_window_layout(cipher_table, message):
    window_layout = [   sg.VPush(),
                        # [sg.Push(), cipher_table[0],sg.Push()],
                        sg.HorizontalSeparator(),
                        # [sg.Push(), cipher_table[1], sg.Push()],
                        [sg.Push(),sg.Text(message),sg.Push()],
                        [sg.Input(key='-IN-')],
                        [sg.Button("Submit")],
                        sg.VPush()]
    key_layout = cipher_table[0]
    value_layout = cipher_table[1]
    key_layout.insert(0, sg.Push())
    key_layout.append(sg.Push())
    value_layout.insert(0, sg.Push())
    value_layout.append(sg.Push())
    window_layout.insert(1, key_layout)
    window_layout.insert(3, value_layout)
    return window_layout

def play():
    cipher_dict = get_encrypted_alphabet()
    table = make_table(cipher_dict)
    layout = get_window_layout(table, MESSAGE)
    window = sg.Window("PySimpleGUI Test", layout, resizable=True)
    window.read(close=True)
play()