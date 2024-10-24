import re

def process(test):
    pattern = r'\b(\w+)\b(\s+\1\b)+'
    matches = re.sub(pattern, r'\1', test)
    matches = matches.split()
    return matches