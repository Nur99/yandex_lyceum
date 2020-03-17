def fractal_print(fractal):
    print('[', end='')
    index = 0
    for element in fractal:
        if index != 0:
            print(', ', end='')
        index += 1
        print(element, end='')
    print(']')

	
def fractal_print(obj):
    print(obj[:])
