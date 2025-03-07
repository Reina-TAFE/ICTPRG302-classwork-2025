# Decisions
#
# Short script to demonstrate decisions operators
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-14
#

print("What is the weather today?")
weather = input("Rain (R), Hot(H): ").upper()
if weather == "R":
    print("It's raining today \nRemember to bring an umbrella!")
elif weather == "H":
    print("Remember to put sunblock on. \nRemember to wear a hat!")
else:
    print("I didn't understand your weather condition.")
print("Hope you have a lovely day")
