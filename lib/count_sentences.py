#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use setter to validate

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Split on ., !, or ? and remove empty/whitespace-only items
        sentences = re.split(r'[.!?]', self._value)
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)
