
def find_all_occurrences(target_word):
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
    >>> find_all_occurrences("world")
    {'w': [0], 'o': [1], 'r': [2], 'l': [3], 'd': [4]}

    >>> find_all_occurrences("hello")
    {'h': [0], 'e': [1], 'l': [2, 3], 'o': [4]}

    >>> find_all_occurrences("hilly")
    {'h': [0], 'i': [1], 'l': [2, 3], 'y': [4]}
    """

    letter_dict = {}
    letter_list = list(target_word)
    for letter_position in range(len(letter_list)):
        if letter_list[letter_position] not in letter_dict.keys():
            letter_dict[letter_list[letter_position]] = [letter_position]
        else:
            letter_dict[letter_list[letter_position]].append(letter_position)
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
    >>> score_guess2()("world", "world")
    [2, 2, 2, 2, 2]

    >>> score_guess2("world", "hello")
    [0, 1, 0, 2, 0]

    >>> score_guess2()("hilly", "world")
    {'h': [0], 'i': [1], 'l': [2, 3], 'y': [4]}
    """
    score = [0] * len(guess)
    guess_dict = find_all_occurrences(guess)
    target_dict = find_all_occurrences(target)
    for letter in guess_dict.keys():
        if letter in target_dict.keys() and len(guess_dict[letter]) <= len(target_dict[letter]):
            for position in guess_dict[letter]:
                if position in target_dict[letter]:
                    score[position] = 2
                    target_dict[letter].remove(position)
                else:
                    score[position] = 1
        elif letter in target_dict.keys():
            for position in target_dict[letter]:
                if position not in guess_dict[letter]:
                    for score_position in guess_dict[letter][:len(guess_dict[letter])-1]:
                        score[score_position] = 1
                else:
                    score[position] = 2
    return score

def main(test=True):
    # if test:
    #     import doctest
    #     return doctest.testmod()
    find_all_occurrences("hello")


if __name__ == '__main__':
    print(main(test=False))