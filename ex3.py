import re

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
text2 = "aaaa ae asdfasdfasdf asdf hihi aeouif"
text3 = "Do YoU want to build a snowmannn? Elsa asked"
text4 = """(Yo, left, yo, left) 'cause sometimes you just feel tired, feel weak
(Yo, left, right, left) and when you feel weak
(Yo, left, yo, left) you feel like you wanna just give up
(Yo, left, right, left) but you gotta search within you
(Yo, left, yo, left) try to find that inner strength and just pull that shit out of you
(Yo, left, right, left) and get that motivation to not give up
(Yo, left, yo, left) and not be a quitter, no matter how bad
(Yo, left, right, left) you wanna just fall flat on your face and collapse"""
text5 = "Look, if you had one shot or one opportunity. To seize everything you ever wanted in one moment. Would you capture it or just let it slip?"

process(text1)
process(text2)
process(text3)
process(text4)
process(text5)
