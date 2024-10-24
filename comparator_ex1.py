import ex1_with_re
import ex1_without_re

text1 = "Hello! Today was a great day ;<) ;<) ;<)"
text2 = """For once, my dog ate my homework and I told my story to my teacher.\n
           She laughed and said that: "That was tasty assignment, right? ;<) ;<))))\n
           I also joked: :Yes, it was ;<)\n
           And at the end, I received a zero."""
text3 = "Sometimes, I wonder where the semicolon in Python is ;<);<);<)"
text4 = ";<);<);<);<);<)"
text5 = "After one day of coding in Python, I think that I can become a machine learning dev;<);<)"

str_arr = [text1, text2, text3, text4, text5]

def check():
    for text in str_arr:
        if ex1_with_re.smileCount(text) != ex1_without_re.smileCount(text):
            print("error")
            return
    print("okay")
check()