def swap(first, second):
    #  сделаем копию списка
    third = second[:]
    #  сотрем старое содержимое, заменим на новое
    second.clear()
    second.extend(first)
    #  сотрем старое содержимое, заменим на новое из предварительно сохраненной копии
    first.clear()
    first.extend(third)
