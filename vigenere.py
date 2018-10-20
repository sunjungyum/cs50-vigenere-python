# Sun-Jung Yum
# Problem Set 6
# Vigenere (Python)
# 25 October 2018

import sys
from cs50 import get_string

# Ensures that the usage is correct and key is entirely alphabetical
if len(sys.argv) != 2 or sys.argv[1].isalpha() == False:
    sys.exit("Usage: python vigenere.py k")

# Declares a string variable for the key that is uppercase since case doesn't matter
keyword = sys.argv[1].upper()

# Declares an int variable to keep track of which character in the keyword should be used
counter = 0

# Prompts for the plain text
plaintext = get_string("plaintext: ")
print("ciphertext: ", end="")

# Iterates through each character of the plaintext
for p in plaintext:
    if p.isalpha():
        # Determines numerical key based on counter
        numkey = ord(keyword[counter % len(keyword)]) - 65

        # Rotates characters as uppercase characters
        upper = p.upper()
        alphabeticalindex = ord(upper) - 65

        # Uses a separate variable called "result" because p's case needs to be checked
        result = 65 + ((alphabeticalindex + numkey) % 26)

        # Converts it back to a separate char (if original was lowercase, returns back to lowercase)
        if p.islower():
            c = chr(result).lower()
        else:
            c = chr(result)

        # Increments keycounter by 1 if the char was alphabetical and rotated
        counter += 1

    # If char is not alphabetical, it remains the same
    else:
        c = p

    # Prints either the alphabetical rotated character or the nonalphabetical character as is
    print(c, end="")

# Prints empty line
print("")