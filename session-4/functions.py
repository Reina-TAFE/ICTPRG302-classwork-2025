# Temperature converter
#
# Manually converts integer from base 10 to binary
#
# Author: Reina Rowlands (20066312)
# Date: 2025-02-28
#

# Ask for temperature
def convert_temperature():
    temperature = int(input("What is the temperature? "))

    # Ask for unit
    unit = input("Celsius (C) or Fahrenheit (F): ").upper()

    if unit == "F":
        converted_temperature = (temperature - 32) * 9/5
        converted_unit = "C"
    elif unit == "C":
        converted_temperature = temperature * 9/5 + 32
        converted_unit = "F"
    else:
        print("Not a valid unit.")
        quit()

    print(f"{temperature} {unit} is equal to {converted_temperature} {converted_unit}")
    return

while True:
    if input("Convert?"):
        convert_temperature()
    else:
        quit()