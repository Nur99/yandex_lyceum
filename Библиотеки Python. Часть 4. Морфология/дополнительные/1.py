import pymorphy2

word = input().strip()
morph = pymorphy2.MorphAnalyzer()
word = morph.parse(word)[0]
time = {("past", "Прошедшее"): ("masc", "femn", "neut", "plur"),
        ("pres", "Настоящее"): {"1per": ("sing", "plur"), "2per": ("sing", "plur"), "3per": ("sing", "plur")}}
if 'VERB' not in word.tag and "INFN" not in word.tag:
    print("Не глагол")
else:
    for key, value in time.items():
        print(f"{key[1]} время:")
        if isinstance(value, dict):
            for value_key, value_value in value.items():
                for j in value_value:
                    print(f"{word.inflect({key[0], value_key, j}).word}")
        else:
            for j in value:
                print(f"{word.inflect({key[0], j}).word}")
