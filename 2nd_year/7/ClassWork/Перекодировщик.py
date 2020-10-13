t = open('cyrillic.txt', encoding='utf8').read()

tr = {
    'й': 'j', 'ц': 'c', 'у': 'u', 'к': 'k', 'е': 'e', 'н': 'n',
    'г': 'g', 'ш': 'sh', 'щ': 'shh', 'з': 'z', 'х': 'h', 'ъ': '#',
    'ф': 'f', 'ы': 'y', 'в': 'v', 'а': 'a', 'п': 'p', 'р': 'r',
    'о': 'o', 'л': 'l', 'д': 'd', 'ж': 'zh', 'э': 'je', 'я': 'ya',
    'ч': 'ch', 'с': 's', 'м': 'm', 'и': 'i', 'т': 't', 'ь': "'",
    'б': 'b', 'ю': 'ju', 'ё': 'jo',
}

for k, v in list(tr.items()):
    tr[k.upper()] = v[0].upper() + v[1:]

tr_text = "".join((tr[c] if c in tr else c for c in t))

f = open('transliteration.txt', 'wt', encoding='utf8')
f.write(tr_text)
f.close()
