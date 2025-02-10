#!/usr/bin/env python3
"""Functions that convert and classify temperatures.

Usage:
    ./temp_functions.py

Author:
    Lukas Rhoades - 9.2.2025
"""

def fahr_to_celsius(temp_fahrenheit):
    """Converts a temperature in fahrenheit to a temperature in celsius.

    temp_fahrenheit <numerical>
        input a temperature in fahrenheit

    returns
    <float>
        a temperature in celsius
    """
    converted_temp = (temp_fahrenheit - 32) / 1.8 # inputs temp in fahrenheit into formula
    return converted_temp                         # returns temp in celsius

def temp_classifier(temp_celsius):
    """Classifies temperatures in celsius into 0, 1, 2, or 3 based on temperature band criteria.

    temp_celsius
        input a temperature in celsius

    returns
    <integer>
        a temperature classified as 0, 1, 2, or 3
    """
    # return 0 if temp is less than 2 degrees celsius
    if temp_celsius < -2:
        return 0
    # return 1 if temp is -2 degrees celsius or warmer but cooler than 2 degrees celsius
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    # return 2 if temp is 2 degrees celsius or warmer but cooler than 15 degrees celsius
    elif temp_celsius >= 2 and temp_celsius < 15:
        return 2
    # return 3 if temp is 15 degrees celsius or warmer
    else:
        return 3