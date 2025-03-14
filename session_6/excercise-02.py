value_dictionary = {
    1: "Hello",
    2: "Goodbye",
    3: "Who is this?"
}

while True:
    user_number = input("Enter a number: ")
    try:
        user_number = int(user_number)
    except ValueError:
        print("Not a number")
        break
    if user_number in list(value_dictionary.keys()):
        print("Found it!")
        print(value_dictionary[user_number])
