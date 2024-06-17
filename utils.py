import re

def only_numbers(text):
    return re.sub(r'[^0-9]', '', text)
