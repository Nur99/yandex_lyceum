def quarter(xcoord, ycoord): 
    xcoord = float(xcoord)
    ycoord = float(ycoord)
    if (xcoord > 0) and (ycoord < 0):
        print("IV четверть")
    elif (xcoord > 0) and (ycoord > 0):
        print("I четверть")
    elif (xcoord < 0) and (ycoord < 0):
        print("III четверть")
    else:
        print("II четверть")
