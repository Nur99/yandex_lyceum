import pymorphy2
import sys
from collections import Counter

morph = pymorphy2.MorphAnalyzer()
abc = 'ёйцукенгшщзхъфывапролджэячсмитьбю \n'
data = sys.stdin.read().lower().replace("-", " ")

words = "".join([c for c in data if c in abc]).split()
s = []
for word in words:
    m = morph.parse(word)[0]
    if m.tag.POS == "NOUN" and m.score > 0.5:
        s.append(m.normal_form)

mc = Counter(s).most_common()
mc.sort(key=lambda x: (x[1], x[0]), reverse=True)
res = [w for w, c in mc]
print(" ".join(res[:10]))
