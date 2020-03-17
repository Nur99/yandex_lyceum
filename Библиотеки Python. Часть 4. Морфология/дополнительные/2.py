import sys

import pymorphy2

data = sys.stdin.readlines()
morph = pymorphy2.MorphAnalyzer()
word2 = morph.parse("живое")[0]
for word in data:
    word = word.strip()
    parsed = morph.parse(word)
    noun_word = None
    for variant in parsed:
        if 'NOUN' in variant.tag:
            noun_word = variant
            break
    if not noun_word:
        print("Не существительное")
        continue
    gender = variant.tag.gender
    number = variant.tag.number
    # print(number, gender)
    if variant.tag.animacy == "anim":
        if number == "plur":
            print(word2.inflect({'ADJF', number}).word.capitalize())
        else:
            print(word2.inflect({'ADJF', gender}).word.capitalize())
    else:
        if number == 'plur':
            print(f"Не {word2.inflect({'ADJF', number}).word}")
        else:
            print(f"Не {word2.inflect({'ADJF', gender}).word}")
