from random import choice

with open('lines.txt', encoding='utf8') as f:
    text = f.readlines()

if text:
    print(choice(text))
