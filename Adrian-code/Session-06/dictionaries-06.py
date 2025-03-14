products  = {
    "Apples": 5,
    "Oranges":6,
    "Pears": 3
}

for item in products:
    print(item, products[item])

print()
# A more elegant method
for item, quantity in products.items():
    print(item, quantity)
