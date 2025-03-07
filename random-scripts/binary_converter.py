# Binary Converter
#
# Manually converts integer from base 10 to binary
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-14
#

def get_binary_length(base10):
    length = 0
    while 2 ** length - 1 < base10:
        length += 1
    return length


def fill_binary_array(base10):
    binary_array = []
    total_positions = get_binary_length(base10)
    for position in range(0, total_positions):
        binary_array.append("0")
    return binary_array


def calculate_binary(base10):
    empty_binary = fill_binary_array(base10)
    output = ""
    binary_total = 0
    total_positions = len(empty_binary)
    for position in range(0, total_positions):
        if binary_total + (2 ** (total_positions - 1 - position)) > base10:
            empty_binary[position] = 0

        else:
            empty_binary[position] = 1
            binary_total += (2 ** (total_positions - 1 - position))
        output += str(empty_binary[position])
    return output


base_10 = int(input("enter an integer: "))
binary = calculate_binary(base_10)
print(binary)
print(bin(base_10))
