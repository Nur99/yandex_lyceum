import json

with open('cats_2.json') as cat_file:
    f = cat_file.read()
    data = json.loads(f)
    for item in data:
        for key, value in item.items():
            if type(value) == list:
                print(f'{key}: {", ".join(value)}')
            else:
                print(f'{key}: {value}')
        print()
