groceries = {}

while True:
    product = input("Item: ").lower()
    if product == "":
        break
    parts = product.split()
    item = parts[0]

    try:
        quantity = int(parts[1])
    except:
        print("Please enter a product and quantity")
        break

    if item in groceries:
        groceries[item] = groceries[item] + quantity
    else:
        groceries[item] = quantity

    print(groceries)
    print(groceries.get("John", "No John's found"))