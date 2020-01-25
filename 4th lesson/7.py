def privet(value):
    addition = [1, 2]
    value = value + addition
    # В данном случае значение value будет локальным


def privett(value):
    addition = [1, 2]
    value += addition
    #  А в данном случае - глобальным


value = [5, 4]
privet(value)
print(*value)
privett(value)
print(*value)
