# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:15:36 2024

@author: USER OS
"""

def is_vowel(character):
    """Check if the given character is a vowel."""
    vowels = "aeiou"
    return character.lower() in vowels

# Get user input
char = input("Enter a single alphabet: ").strip()

if len(char) == 1 and char.isalpha():
    if is_vowel(char):
        print(f"{char.upper()} is a vowel.")
    else:
        print(f"{char.upper()} is not a vowel.")
else:
    print("Invalid input. Please enter a single alphabet.")