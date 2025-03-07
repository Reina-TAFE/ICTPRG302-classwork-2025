# Temperature Converter
#
# Filename: temperature-converter.py
# Author:   Adrian Gould
# Date:     2025-02-28

def temperature_converter(temp, unit):
    # If Celsius then
    if unit == "C":
        # Fahrenheit is Celsius * 9 / 5 + 32
        converted = temp * 9 / 5 + 32
    # Else
    else:
        # Celsius is (Fahrenheit - 32) * 5 / 9
        converted = (temp - 32) * 5 / 9
    # End if
    return converted


def scale_converter(unit):
    # Scale Converter
    if unit == "C":
        converted = "F"
    else:
        converted = "C"
    return converted


# Ask for the temperature
temperature = float(input("Temperature: "))

# Ask for the scale (Celsius, Fahrenheit)
scale = input("From Celsius (C) or Fahrenheit (F): ")
scale = scale.upper()

# Call the temperature & scale converters
converted_temperature = temperature_converter(temperature, scale)
converted_scale = scale_converter(scale)

# Display Converted Temperature
print(temperature, scale, "is ", converted_temperature, converted_scale)
