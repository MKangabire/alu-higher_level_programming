#!/usr/bin/python3
"""
e a function that prints a text with 2 new lines after each of these character
"""


def text_identation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    separators = ['.', '?', ':']
    sentences = []
    current_sentence = ''
    
    for char in text:
        current_sentence += char
        if char in separators:
            sentences.append(current_sentence.strip())
            current_sentence = ''
    
    for sentence in sentences:
        print(sentence)
