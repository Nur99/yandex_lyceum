line1, line2 = input(), input()
if line1 == line2:
    print('ничья')
elif (line1 == 'бумага' and line2 == 'камень') or (line1 == 'камень' and line2 == 'ножницы'): 
    print('первый')
elif (line1 == 'ножницы' and line2 == 'бумага') or (line1 == 'ром' and line2 == 'пират'):
    print('первый')
elif (line1 == 'ром' and line2 == 'бумага') or (line1 == 'пират' and line2 == 'камень'):
    print('первый')
elif (line1 == 'ножницы' and line2 == 'ром') or (line1 == 'пират' and line2 == 'ножницы'):
    print('первый')
elif (line1 == 'камень' and line2 == 'ром') or (line1 == 'бумага' and line2 == 'пират'):
    print('первый')   
else:
    print('второй')
