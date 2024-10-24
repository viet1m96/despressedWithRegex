import re

def smileCount(text):
    pattern = r';<\)'
    matches = re.findall(pattern, text)
    return len(matches)

