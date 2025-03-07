# Temperature Converter
#
# Filename: temperature-converter.py
# Author:   Adrian Gould
# Date:     2025-02-28

# Ask for the temperature
temperature = float(input("Temperature: "))

# Ask for the scale (Celsius, Fahrenheit)
scale = input("From Celsius (C) or Fahrenheit (F): ")
scale = scale.upper()

# If Celsius then
if (scale == "C"):
    # Fahrenheit is Celsius * 9 / 5 + 32
    converted_temperature = temperature * 9 / 5 + 32
# Else
else:
    # Celsius is (Fahrenheit - 32) * 5 / 9
    converted_temperature = (temperature - 32) * 5 / 9
# End if

# Display Converted Temperature
if (scale == "C"):
    converted_scale = "F"
else:
    converted_scale = "C"

print(temperature, scale, "is ", converted_temperature, converted_scale)