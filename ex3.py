import functools
import re

def cmp(a: str, b: str) -> bool:
    if len(a) < len(b): return True
    if len(a) > len(b): return False
    return a < b

def process(test):
    pattern = r'\b[^euoaiEUOAI\s]*([euoaiEUOAI])([^euoaiEUOAI\s]*\1*)*\b'
    matches = re.finditer(pattern, test)
    matches = list(matches)
    matches = [match.group() for match in matches]
    sorted_grp = sorted(matches, key=lambda x: (len(x), x))
    for match in sorted_grp:
        print(match, end = " ")
    print()

text1 = "Today was a good day for me, I wanna to flyyyyyy."
text2 = "aaaa ae asdfasdfasdf asdf hihi"
text3 = "Do YoU want to build a snowmannn? Elsa asked"
text4 = "Happy new year Happyyy birthday, Haloween day"
text5 = "Look, if you had one shot or one opportunity. To seize everything you ever wanted in one moment. Would you capture it or just let it slip?"

process(text1)
process(text2)
process(text3)
process(text4)
process(text5)
