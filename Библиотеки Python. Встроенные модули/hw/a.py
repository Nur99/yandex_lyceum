from random import sample
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789'


def generate_password(m):
    return ''.join(sample(symbols, m))
 

def main(n, m):
    a = set()
    while len(a) < n:
        a.add(generate_password(m))
    return a
 
