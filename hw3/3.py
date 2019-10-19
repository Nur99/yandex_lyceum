a = input()

if int(a) % 4 == 0 and int(a) % 100 != 0:

    print('Високосный')

elif int(a) % 400 == 0:

    print('Високосный')

else:

    print('Не високосный')
