def score(zone, n=0):
    global scoring
    if n == 0:
        return scoring[zone]
    else:
        return scoring[zone][n]
