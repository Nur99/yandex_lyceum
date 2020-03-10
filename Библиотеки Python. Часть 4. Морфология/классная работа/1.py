import pymorphy2
import sys

morph = pymorphy2.MorphAnalyzer()
input_data = sys.stdin.read().lower()
abc = 'ёйцукенгшщзхъфывапролджэячсмитьбю \n'

words = "".join([c for c in input_data if c in abc]).split()
count = 0
for word in words:
    if morph.parse(word)[0].normal_form in ["видеть", "увидеть", "глядеть", "примечать", "узреть"]:
        count += 1
print(count)
