# Warm up.
#
# Number guessing game.
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-21
#
play = True
while play:
    text = input("write something: ")
    letter = input("pick a letter: ")
    found = False

    for character in text:
        if character == letter:
            found = True
            break

    if found:
        print("yes", letter, "is in your text")
    else:
        print(letter, "is not in your text")

    if text.find(letter) != -1:
        print("yes", letter, "is in your text")
    else:
        print(letter, "is not in your text")

    if input("would you like to continue? y/n \n").lower() == "y":
        continue
    else:
        play = False