'''
PROBLEM:
Write a unique_characters() function that determines if any
given string has all unique characters (i.e. no character in
the string is duplicated). If the string has all unique characters,
the function should return True. If the string does not have 
all unique characters, return False.

For example, unique_characters("apple") should return False.
'''
def unique_characters(string_in):
    duplicate_letters = set()
    for letter in string_in:
        if letter not in duplicate_letters:
            duplicate_letters.add(letter)
            continue
        return False
    return True

print(unique_characters("letter"))