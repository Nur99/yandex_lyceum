import random


def make_bingo():
    s24 = random.sample(range(1, 76), 24)
    res = s24[:12] + [0] + s24[12:]    
    return tuple(res[:5]), tuple(res[5:10]), tuple(res[10:15]), tuple(res[15:20]), tuple(res[20:])

