import time


def score_guess1(guess, target):
    """
    Compares each letter of guess and target to see if they are the same.
    If guess letter and target letter do not match, checks if target
    word contains guess letter.

    Parameters
    ----------
    guess : string
    target : string

    Returns
    -------
    result : a list of integer numbers of length len(target)

    Examples
    --------
    >>> score_guess("world", "world")
    ['2', '2', '2', '2', '2']

    >>> score_guess("world", "hello")
    ['0', '1', '0', '2', '0']

    score_guess("hilly","world")
    ['0', '0', '0', '2', '0']
    """

    # Set score to list of 0's of length len(target)
    score = ['0'] * len(target)

    # Repeat for each letter position 'index' of guess
    for index in range(len(guess)):
        guess_letter = guess[index]  # Set guess_letter to letter in current index of guess

        # If guess_letter matches target letter at current position,
        # set current position of score to 2
        if guess_letter == target[index]:
            score[index] = '2'
        else:
            for target_letter in target:
                if guess_letter == target_letter:
                    score[index] = '1'
    return score


def find_all_occurrences(word):
    """Returns a dictionary of letters in target_word, with each unique letter as the keys
    and a list of the position(s) of each occurrence as the values

     Parameters
    ----------
    word : string

    Returns
    -------
    result : dictionary of letter (string) : [occurrences] (List of ints) as key: value pairs

    Examples
    --------
    >>> find_all_occurrences("world")
    {'w': [0], 'o': [1], 'r': [2], 'l': [3], 'd': [4]}

    >>> find_all_occurrences("hello")
    {'h': [0], 'e': [1], 'l': [2, 3], 'o': [4]}

    >>> find_all_occurrences("hilly")
    {'h': [0], 'i': [1], 'l': [2, 3], 'y': [4]}
    """

    letter_dict = {}
    for position, letter in enumerate(list(word)):
        if letter not in letter_dict.keys():
            letter_dict[letter] = [position]
        else:
            letter_dict[letter].append(position)
    return letter_dict


def score_guess2(guess, target):
    """Compares letters in guess and target, and returns the score as a
    list of integers

     Parameters
    ----------
    guess : string
    target : string

    Returns
    -------
    score : list of integers

    Examples
    --------
    >>> score_guess2("match", "world")
    [0, 0, 0, 0, 0]

    >>> score_guess2("coast", "tacos")
    [1, 1, 1, 1, 1]

    >>> score_guess2("world", "world")
    [2, 2, 2, 2, 2]

    >>> score_guess2("world", "hello")
    [0, 1, 0, 2, 0]

    >>> score_guess2("hilly", "world")
    [0, 0, 0, 2, 0]

    >>> score_guess2("petal", "hello")
    [0, 2, 0, 0, 1]

    >>> score_guess2("hilly", "hello")
    [2, 0, 2, 2, 0]

    >>> score_guess2("lulls", "world")
    [0, 0, 0, 2, 0]
    """

    # create score list
    score = [0] * len(guess)

    # get letter position dict for guess and target
    guess_dict = find_all_occurrences(guess)
    target_dict = find_all_occurrences(target)

    # loop for each unique letter in guess
    for letter in guess_dict.keys():
        # if letter is in target and has fewer or equal occurrences as letter in target
        if letter in target_dict.keys() and len(guess_dict[letter]) <= len(target_dict[letter]):
            # test each position that letter occurs in guess
            for position in guess_dict[letter]:
                # test if position matches an occurrence of letter in target
                if position in target_dict[letter]:
                    # if target has an occurrence of letter at position, set position of score to 2
                    score[position] = 2
                    # target_dict[letter].remove(position)
                else:
                    # if position doesn't match an occurrence position of letter in target
                    # set position of score to 1
                    score[position] = 1

        # test if letter is in target
        elif letter in target_dict.keys():
            # (if this point is reached, guess has more occurrences of letter than target)

            # loop for each index of target_dict[letter]
            for index in range(len(target_dict[letter])):
                # set target position to current occurrence position
                position = target_dict[letter][index]
                # test if target letter position has occurrence in guess
                if position in guess_dict[letter]:
                    score[position] = 2

                # test if current occurrence of letter in guess is not between current and final
                # occurrences in target
                elif guess_dict[letter][index] < position or guess_dict[letter][index] > max(target_dict[letter]):
                    score[position] = 1
    return score


def main(test=True):
    # if test:
    #     import doctest
    #     return doctest.testmod()
    find_all_occurrences("hello")

    result = score_guess2("bobby", "blobs")

    print(f"{result}")


if __name__ == '__main__':
    print(main(test=False))
