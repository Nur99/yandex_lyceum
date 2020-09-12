line1, line2 = input(), input()
if line1 == line2:
    print('ничья')
elif (line1 == 'бумага' and line2 == 'камень') or (line1 == 'камень' and line2 == 'ножницы'): 
    print('первый')
elif line1 == 'ножницы' and line2 == 'бумага':
    print('первый')
else:
    print('второй')
