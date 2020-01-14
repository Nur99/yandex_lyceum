def late(now, classes, bus):
    now_min = int(now.split(':')[0]) * 60 + int(now.split(':')[1])
    classes_min = int(classes.split(':')[0]) * 60 + int(classes.split(':')[1])
    for t in bus[::-1]:
        if ((t >= 5) & (classes_min - now_min - 15 - t >= 0)):
            return 'Выйти через ' + str(t - 5) + ' минут'
    return 'Опоздание'
