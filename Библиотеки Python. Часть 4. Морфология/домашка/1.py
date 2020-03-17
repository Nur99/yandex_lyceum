import pymorphy2

bottles = 99
morph = pymorphy2.MorphAnalyzer()
word = morph.parse('бутылка')[0]
word2 = morph.parse("Осталось")[0]
while bottles > 0:
    print(f'В холодильнике {bottles} {word.make_agree_with_number(bottles).word} кваса.')
    print('Возьмём одну и выпьем.')
    bottles -= 1
    print(f"""{word2.inflect(
        {'VERB', 'perf', 'intr', 'past', 'femn' if bottles % 10 == 1 
                                                   and bottles != 11 else 'indc'}).word.capitalize()
        } {bottles} {word.make_agree_with_number(bottles).word} кваса.""")
