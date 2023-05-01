n = int(input())  # تعداد کلمات در دیکشنری
dictionary = {}  # دیکشنری برای ذخیره ترجمه‌ها
for i in range(n):
    word, eng, fr, de = input().split()
    dictionary[word] = {'en': eng, 'fr': fr, 'de': de}

sentence = input().split()  # خواندن جمله

src_lang = input().strip()  # خواندن زبان مبدا
if src_lang == 'en':
    dest_lang = 'fr'  # زبان مقصد ترجمه
elif src_lang == 'fr':
    dest_lang = 'de'
else:
    dest_lang = 'en'

translated_sentence = []  # لیستی برای ذخیره ترجمه‌ی جمله
for word in sentence:
    if word in dictionary:
        translated_word = dictionary[word][dest_lang]
    else:
        translated_word = word  # در صورت عدم وجود ترجمه، کلمه را خودش بازگردانی می‌کنیم
    translated_sentence.append(translated_word)

output = ' '.join(translated_sentence)  # ترکیب ترجمه‌ی کلمات به یک جمله
print(output)