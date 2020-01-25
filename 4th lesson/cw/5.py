def mirror(arr):
    mirrored_part = reversed(arr)
    # Если это было = arr.reverse(), то в переменной не было бы значения
    arr += mirrored_part
    # Если не будет +=, то arr станет локальной, т.е элементы не прибавятся
