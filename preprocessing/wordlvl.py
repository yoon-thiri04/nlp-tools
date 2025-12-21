from myword import SyllableTokenizer,WordTokenizer

text = "အင်တာနက်နည်းပညာသည် ကမ္ဘာတစ်၀န်းသို့ အချက်အလက်များ ပေးပို့ရန် အလွယ်ကူဆုံးနည်းလမ်းဖြစ်လာသည်။ လူတိုင်းသည် အွန်လိုင်းပေါ်တွင် သတင်းအချက်အလက်ကို လွယ်ကူစွာ ရရှိနိုင်သည်။"
text2= "ငါ့ကြောင့်ဖြစ်တာလား ကျောင်းကြောင့်နှင့်မောင့်အောင့်၎င်းကိုနှင့် မျော်ကိုး၍ စောင့်ဆိုင်းငရုတ်ကောင်း"
#syltok = SyllableTokenizer()
#print(syltok.tokenize(text))

wordtok = WordTokenizer()
tokenize= wordtok.tokenize(text)
<<<<<<< HEAD
line=" ".join(tokenize)
with open("D:/python_hand_face_testing/nlp/preprocessing/word_output.txt","w",encoding="utf-8") as f:
    f.write(line)
=======

syltok = SyllableTokenizer()
tokenize_syl = syltok.tokenize(text2)
line=" ".join(tokenize_syl)
print(line)
with open("syloutput.txt","w",encoding="utf-8") as f:
    f.write(line)
>>>>>>> a754503 ( update)
