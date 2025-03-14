names = {}

while True:
    name = input("Name: ")
    if name == "":
        break
    elif name in names:
        names[name] += 1
    else:
        names[name] = 1
print(names)
