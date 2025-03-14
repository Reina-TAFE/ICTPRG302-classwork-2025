names = {}

while True:
    name = input("Name: ")
    if name == "":
        break
    else:
        names[name] = names.get(name, 0) + 1

print(names)

print(names.get("John", "No John's found"))
