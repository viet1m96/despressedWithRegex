import ex2_with_re
import ex2_without_re

text1 = """Довольно распространённая ошибка ошибка – это лишний повтор повтор слова слова. Смешно, не не правда ли? Не нужно портить хор хоровод."""
text2 = "alo alo, can you hear me?"
text3 = "asdf asdf asdf asdf asdf\naha\nasdf"
text4 = """For once, my dog ate my homework and I told my story to my teacher.
           She laughed and said that: "That was tasty assignment, right?
           I also joked: :Yes, it was was ;
           And at the end, I received a zero."""
text5 = """After passing the test with flying colors, I screammmmmmm: Huraa Huraa Huraa """

str_arr = [text1, text2, text3, text4, text5]

def check():
    for text in str_arr:
        if ex2_with_re.process(text) != ex2_without_re.process(text):
            print("error")
            return
    print("okay")
check()