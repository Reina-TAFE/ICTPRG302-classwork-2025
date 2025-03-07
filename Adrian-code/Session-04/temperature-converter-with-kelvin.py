# Temperature Converter with C, F and K
#
# Filename: temperature-converter-with-kelvin.py
# Author:   Adrian Gould
# Date:     2025-02-28

# Ask for the temperature
temperature = float(input("Temperature: "))

# Ask for the scale to convert from (Celsius, Fahrenheit or Kelvin)
scale_from = input("From Celsius (C), Fahrenheit (F) or Kelvin (K): ")
scale_from = scale_from.upper()

# Ask for the scale to convert to (Celsius, Fahrenheit or Kelvin)
scale_to = input("To Celsius (C), Fahrenheit (F) or Kelvin (K): ")
scale_to = scale_to.upper()

converted_temperature = "ERROR"

# If Celsius then
if scale_from == "C" and scale_to == "F":
    # Fahrenheit is Celsius * 9 / 5 + 32
    converted_temperature = temperature * 9 / 5 + 32
    converted_scale = "C"

elif scale_from == "F" and scale_to == "C":
    # Celsius is (Fahrenheit - 32) * 5 / 9
    converted_temperature = (temperature - 32) * 5 / 9
    converted_scale = "F"

elif scale_from == "K" and scale_to == "C":
    converted_temperature = temperature - 273.16
    converted_scale = "C"

elif scale_from == "C" and scale_to == "K":
    converted_temperature = temperature + 273.16
    converted_scale = "K"

elif scale_from == "F" and scale_to == "K":
    converted_temperature = (temperature - 32) * 5 / 9 + 273.16
    converted_scale = "K"

elif scale_from == "K" and scale_to == "F":
    converted_temperature = (temperature - 273.16) * 9 / 5 + 32
    converted_scale = "F"

else:
    print("ERROR: Unknown scale")
# End if


print(temperature, scale_from, "is ", converted_temperature, scale_to)