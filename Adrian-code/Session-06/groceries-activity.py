groceries = {}

while True:
    # User enters: Apples 4
    product = input("Product & Quantity: ").lower()
    if product == "":
        break
    parts = product.split()
    item = parts[0]

    try:
        quantity = int(parts[1])
    except:  # catches ALL error types, not best practice
        print("Please enter a product and quantity")
        quantity = 0

    if item in groceries:
        groceries[item] = groceries[item] + quantity
    elif quantity>0:
        groceries[item] = quantity

print(groceries)
