a = input()

b = input()

c = a + b

if a == 'Пенза' or b == 'Тула' or not(a == 'Тула' or b == 'Пенза') or c == 'ТулаПенза':

    print('НЕТ')

else:

    print('ДА')
