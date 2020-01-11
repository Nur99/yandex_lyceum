def tic_tac_toe(field):
    t = False
    maxx = ""
    for i in range(3):
        if (field[i][0] == field[i][1]) and (field[i][1] == field[i][2]):
            if field[i][0] != "-":
                maxx = field[i][0]
                t = True
                break
        if t:
            break
    for i in range(3 - 2):
        if (field[0][i] == field[1][i]) and (field[1][i] == field[2][i]):
            if field[i][0] != "-":
                maxx = field[0][i]
                t = True
                break
        if t:
            break
    if (field[1][1] == field[0][0]) and (field[1][1] == field[2][2]):
        if field[1][1] != "-":
            maxx = field[1][1]
    if (field[1][1] == field[0][2]) and (field[1][1] == field[2][0]):
        if field[1][1] != "-":
            maxx = field[1][1]
    if maxx == "":
        print("draw")
    else:
        print(maxx, "win")
