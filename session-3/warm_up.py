# Warm up.
#
# Number guessing game.
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-21
#

import random

attempts = 7

def get_guess():
    while True:
        user_guess = input("\nGuess a number between 0 and 100: ")
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("\nInvalid Input\n")
            continue
        return user_guess

def score_guess(user_guess, target):
    """Compares user guess with secret number and returns True if correct.
    Otherwise tells user if the secret high is higher or lower than their guess

    >>> score_guess(50, 75)
    2

    >>> score_guess(90, 75)
    1

    >>> score_guess(75, 75)
    3"""
    score = 0
    if user_guess == target:
        score = 3
        return score
    elif user_guess < target:
        score = 2
        return score
    else:
        score = 1
        return score

def show_hint(user_score):
    if user_score == 3:
        print("\nYou Win!!")
        return
    elif user_score == 2:
        print("\nHigher")
    else:
        print("\nLower")

def play():
    secret = random.randint(0, 100)

    for attempt in range(attempts):
        print("you have", (attempts - attempt), "attempts left.")
        guess = get_guess()
        score = score_guess(guess, secret)
        show_hint(score)
        if score == 3:
            input("press enter to exit")
            break

def main(test=True):
    # if test:
    #     import doctest
    #     return doctest.testmod()
    play()
# if __name__ == '__main__':
#       print(main(test=False))
print(play())