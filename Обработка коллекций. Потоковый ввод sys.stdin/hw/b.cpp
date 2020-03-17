import sys


def gematry(s):
    return sum(map(lambda ch: ord(ch) - ord('A') + 1, s.upper()))


data = list(map(str.strip, sys.stdin))
print('\n'.join(sorted(data, key=lambda x: (gematry(x), x))))

