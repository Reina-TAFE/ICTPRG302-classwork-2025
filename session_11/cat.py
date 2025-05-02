"""
Documentation Example 1

Author: Reina Rowlands (20066312)
Date: 2025-03-28
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says "Meow!"')

tabby = Cat("Bingus", 1)
black = Cat("Tavi", 7)

print(tabby.name)
print(black.age)

tabby.meow()
