def defractalize(fractal):
    #  метод remove удаляет первое вхожение объекта
    while fractal in fractal:
        fractal.remove(fractal)
