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
    """Returns a dictionary of letters in target_word, with each unique letter as the keys
    and a list of the position(s) of each occurrence as the values

     Parameters
    ----------
    guess : string

    Returns
    -------
    result : dictionary of letter : [occurrences] pairs

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


if __name__ == '__main__':
    print(main(test=False))
