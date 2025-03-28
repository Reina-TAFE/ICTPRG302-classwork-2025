""" Wordle is a game where the player tries to guess a 5-letter word. The player has 6 attempts to guess the word.
After each attempt the player will receive a score for each letter based on if the letter is in the target word and
if the position is correct. ⬜(0) = incorrect letter 🟨(1) = correct letter, wrong position 🟩(2) = correct letter,
correct position

Author: Reina Rowlands
Company: Reina Rowlands
Copyright: 2023"""

import random



VALID_WORDS_LIST = open("./word-bank/all_words.txt")
TARGET_WORDS_LIST = open('./word-bank/target_words.txt')
VALID_WORDS = (VALID_WORDS_LIST.read()).split()
TARGET_WORDS = (TARGET_WORDS_LIST.read()).split()
VALID_WORDS_LIST.close()
TARGET_WORDS_LIST.close()

MAX_Attempts = 6


def show_instructions():
    """Try to guess the target 5-letter word!
    You have 6 attempts to guess. After each guess you will be given a hint:
    🟩 = correct letter + correct place
    🟨 = correct letter but in the wrong place
    ⬜ = incorrect letter (not in the target word)"""
    return None


def score_guess(guess_list, target_list):
    """takes the user guess and target word as a list of letters for each word
    and compares each letter of the guess to the target to see if the target contain the letter and if the letter is in the same position.
    Returns the score as a list with each position corresponding to the letter of the guess


    >>> score_guess(['H', 'E', 'L', 'L', 'O'], ['h', 'e', 'l', 'l', 'o'])
    [2, 2, 2, 2, 2]
    
    >>> score_guess(['H', 'E', 'L', 'L', 'O'], ['c', 'r', 'a', 'n', 'e'])
    [0, 1, 0, 0, 0]
    
    >>> score_guess(['H', 'E', 'L', 'L', 'O'], ['h', 'z', 'z', 'z', 'z'])
    [2, 0, 0, 0, 0]
    
    >>> score_guess(['H', 'E', 'L', 'L', 'O'], ['z', 'h', 'z', 'z', 'z'])
    [1, 0, 0, 0, 0]
    
    >>> score_guess(['H', 'E', 'L', 'L', 'O'], ['H', 'E', 'L', 'L', 'O'])
    [2, 2, 2, 2, 2]
    
    >>> score_guess(['H', 'E', 'L', 'L', 'O'], ['w', 'o', 'r', 'l', 'd'])
    [0, 0, 0, 2, 1]"""
    #in class activity
    score = [0, 0, 0, 0, 0]
    count = 0
    for letter in guess_list:
        guess_list[count] = letter.lower()
        target_list[count] = target_list[count].lower()
        count += 1

    for position in range(0, len(guess_list)):
        if guess_list[position].lower() == target_list[position].lower():  # tests if letter matches target letter in the same position
            score[position] = 2  # sets score for letter position to 2 (correct)
            target_list[position] = '~'
            guess_list[position] = '~'
        # position += 1

    count = 0
    for letter in guess_list:  # tests each letter in guess
        if letter != '~':
            if letter in target_list:  # tests if letter is in the target word
                score[count] = 1  # if letter does not match target letter, sets score for position to 1 (close)
                target_list.remove(letter)
        count += 1
    return score


def format_score(score):  # Tests score for each position and returns corresponding square
    """takes the score and formats it into coloured squares"""
    formatted_score = [0, 0, 0, 0, 0]
    count = 0
    for num in score:
        if num == 2:
            formatted_score[count] = '🟩'

        elif num == 1:
            formatted_score[count] = '🟨'

        else:
            formatted_score[count] = '⬜'

        count += 1
    return formatted_score


def show_score(guess, score):
    """takes the guess and unformatted score. the score is passed to format_score() and the formatted score is returned.
    the guess and score are then printed"""
    count = 0
    score = format_score(score)  # returns score as white/yellow/green squares
    output_guess = "" # defines output_guess/score variables
    output_score = ""
    for char in guess:  # loops for each letter in guess
        output_guess = output_guess + (" " + str(char))  # adds each letter to a string
        output_score = output_score + str(score[count])  # adds corresponding score to string
        count += 1  # increments position counter by 1
    print(output_guess)  # Displays guess and score
    print(output_score, "\n")
    return


def get_guess():  # get guess for user and test if it is valid
    """takes a guess from the user and checks if it is in the list of valid words.
    if the guess is valid, it is passed back to play() as a string"""
    while True:
        guess_word = input('Make a guess: ')
        if guess_word in VALID_WORDS:
            return guess_word.upper()
        else:
            print('Invalid guess')

def record_stats(username, tries):
    """records usernames and scores in a separate file, user_stats.txt"""
    try:
        with open('./word-bank/user_stats.txt', "x") as stats:
            lines = f"{username}, {tries}"
            stats.writelines(lines)
            stats.close()

    except FileExistsError:
        with open("./word-bank/user_stats.txt", "r") as stats:
            lines = stats.readlines()
            new_lines = list()
            stats.close()
            for line in lines:
                new_user = True
                line.rstrip()
                data = line.split(', ')
                if username == data[0]:
                    new_user = False
                    data.append(str(tries))
                    new_line = ", ".join(data) #source for .join() https://www.digitalocean.com/community/tutorials/python-join-list
                    new_lines.append(new_line)
            if new_user:
                new_line = f"{username}, {tries}"
                new_lines.append(new_line)
            stats.close()
            with open("./word-bank/user_stats.txt", "w") as new_stats:
                new_stats.writelines(new_lines)
                new_stats.close()
    return None
    
def get_average(username):
    """calculates the average number of guesses it takes for a user to win"""
    with open("./word-bank/user_stats.txt", "r") as stats:
        lines = stats.readlines()
        for line in lines:
            line = line.rstrip()
            data = line.split(', ')

            if data[0] == username:     #test if line starts with correct username
                total = 0
                scores = data[1:]       #create list of scores
                for score in scores:
                    total += int(score)
                average = total / len(scores)  #calculate average score
    stats.close()
    return average

def play():
    """defines the order in which to execute the functions"""
    print(show_instructions.__doc__)
    name = input("Hi! Welcome to Wordle, what is your name?\n")
    current_attempt = 1
    target_word = random.choice(TARGET_WORDS).lower()  # selects a word from the target_words file

    while 0 < current_attempt <= MAX_Attempts:  # loops until player runs out of attempts
        guess = get_guess()  # Asks the player for a guess, returns guess as a string
        score = score_guess(list(guess), list(target_word))  # passes both guess and target as lists of letters to score_guess(). returns score list
        print("My guess", guess.upper())
        show_score(guess.upper(), score)  # guess and score list passed to show_score()
        if score == [2, 2, 2, 2, 2]:  # tests if guess is correct
            print("You Win!")            
            if name != '':
                record_stats(name, current_attempt)
                print("Your average number of guesses is: " + str(get_average(name)))
            exit()  # exits program
        else:
            current_attempt += 1  # if guess is incorrect, increments current_attempt by 1 and continues loop
            print("Try Again :( ")
            print("\nYou have", (MAX_Attempts - current_attempt), "attempts remaining\n") # decreases current_attempt by 1
    print("The word was: " + target_word)
    print("You Lose :(")
    exit()


def main(test=True):
    # if test:
    #     import doctest
    #     return doctest.testmod()
    play()


if __name__ == '__main__':
    print(main(test=False))

