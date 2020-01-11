def space_game(text): 
    s = 0
    for i in text:
        if i == " ":
            s += 1
    if s % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
