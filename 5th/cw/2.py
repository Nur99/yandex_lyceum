def choose_сoffee(*preferences):
    global ingredients
    resources = {'Эспрессо': {'beans': 1, 'milk': 0, 'cream': 0},
                 'Капучино': {'beans': 1, 'milk': 3, 'cream': 0},
                 'Кофе по-венски': {'beans': 1, 'milk': 0, 'cream': 2},
                 'Латте Маккиато': {'beans': 1, 'milk': 2, 'cream': 1},
                 'Кон Панна': {'beans': 1, 'milk': 0, 'cream': 1},
                 'Маккиато': {'beans': 2, 'milk': 1, 'cream': 0}}
    beans = ingredients[0]
    milk = ingredients[1]
    cream = ingredients[2]
    for i in preferences:
        one = beans - resources[i]['beans']
        two = milk - resources[i]['milk']
        three = cream - resources[i]['cream']
        if one >= 0 and two >= 0 and three >= 0:
            ingredients[0] -= resources[i]['beans']
            ingredients[1] -= resources[i]['milk']
            ingredients[2] -= resources[i]['cream']
            return i
    return 'К сожалению, не можем предложить Вам напиток'
