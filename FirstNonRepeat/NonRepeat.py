"""
Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample test
"""


class NonRepeat:
    def __init__(self):
        self.string = str()
        self.cleaned = str()

    def set_value(self, string):
        self.string = string
        if self.string:
            self.cleaned = self.string.lower()

    def get_value(self):
        if not self.string:
            return ''
        for character in self.string:
            if self.cleaned.count(character.lower()) == 1:
                return character
        return ''
