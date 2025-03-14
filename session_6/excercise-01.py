dictionary_1 = {1:10, 2:20, 3:30}
dictionary_2 = {4:40, 5:50, 6:60}
dictionary_3 = {7:70, 8:80, 9:90}

# new_dict = dictionary_1 + dictionary_2 + dictionary_3

dictionary_1.update(dictionary_2)
dictionary_1.update(dictionary_3)

print(dictionary_1)