# Temperature Converter with C, F and K
#
# Filename: temperature-converter-with-kelvin.py
# Author:   Adrian Gould
# Date:     2025-02-28

def temperature_C_to_F(temp):
    converted = temp * 9 / 5 + 32
    return converted


def temperature_F_to_C(temp):
    converted = (temp - 32) * 5 / 9
    return converted

def temperature_C_to_K(temp):
    converted = temp -273.16
    return converted

def temperature_K_to_C(temp):
    converted = temp + 273.16
    return converted


def temperature_F_to_K(temp):
    converted = temperature_C_to_K(temperature_F_to_C(temp))
    return converted

def temperature_K_to_F(temp):
    converted = temperature_C_to_F(temperature_K_to_C(temp))
    return converted


def temperature_converter(temp, unit_from, unit_to):
    converted_temperature = temp
    if scale_from == "C" and scale_to == "F":
        converted_temperature = temperature_C_to_F(temp)

    elif scale_from == "F" and scale_to == "C":
        converted_temperature = temperature_F_to_C(temp)

    elif scale_from == "K" and scale_to == "C":
        converted_temperature = temperature_K_to_C(temp)

    elif scale_from == "C" and scale_to == "K":
        converted_temperature = temperature_C_to_K(temp)

    elif scale_from == "F" and scale_to == "K":
        converted_temperature = temperature_F_to_K(temp)

    elif scale_from == "K" and scale_to == "F":
        converted_temperature = temperature_K_to_F(temp)

    else:
        converted_temperature = "ERROR"

    return converted_temperature


# Ask for the temperature
temperature = float(input("Temperature: "))

# Ask for the scale to convert from (Celsius, Fahrenheit or Kelvin)
scale_from = input("From Celsius (C), Fahrenheit (F) or Kelvin (K): ")
scale_from = scale_from.upper()

# Ask for the scale to convert to (Celsius, Fahrenheit or Kelvin)
scale_to = input("To Celsius (C), Fahrenheit (F) or Kelvin (K): ")
scale_to = scale_to.upper()

converted_temperature = temperature_converter(temperature, scale_from, scale_to)

print(temperature, scale_from, "is ", converted_temperature, scale_to)
