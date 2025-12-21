from burmese_tools import tools
from myanmartools import ZawgyiDetector
import re
import unicodedata

detector = ZawgyiDetector()


def normalize_myanmar(text):
    
    text = unicodedata.normalize("NFC", text)
    return text

def convert(text):
    score = detector.get_zawgyi_probability(text)
    if score > 0.95:
        # Use rabbit for conversion
        text_cvt = tools.zaw2uni(text)
        text = normalize_myanmar(text_cvt)
    return text

def uni_to_zawgyi_convert(text):
    return tools.uni2zaw(text)
def sylbreak(text):
    tokens = tools.uni_syllable(text, type=1)
    return tokens

with open("D:/Sem8/my_ai_study/nlp/preprocessing/zawgyi.txt","r",encoding="utf-8")as f:

    uni_text = f.read()


unicode_text = convert(uni_text)

sylbreak_list= sylbreak(unicode_text)
sylbreak_text=" ".join(sylbreak_list)


print(sylbreak_text)
with open("D:/Sem8/my_ai_study/nlp/preprocessing/output1.txt","w",encoding="utf-8") as f:
    f.write(sylbreak_text)


