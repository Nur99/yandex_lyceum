import json

data = [
    {
        "name": "Барсик",
        "age": 7,
        "toys": [
            "Мышка",
            "Прутик",
            "Бантик",
            "Свой хвост"
        ]
    },
    {
        "name": "Мурзик",
        "age": 3,
        "toys": [
            "Рука хозяйки",
            "Шнур от телевизора",
            "Обои на стене"
        ]
    }
]

with open('cats.json', 'w') as file:
    json.dump(data, file)
# with open('cats.json', 'w') as file:
#    json.dump(data, file, ensure_ascii=False)
# with open('cats.json', 'w') as file:
#    json.dump(data, file, ensure_ascii=False, indent=2)
# with open('cats.json', 'w') as file:
#    json.dump(data, file, ensure_ascii=False, indent=2, sort_keys=True)
