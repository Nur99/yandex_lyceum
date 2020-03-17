import sys

data = list(map(lambda x: int(x.strip()), sys.stdin))
if len(data) > 0:
    print(sum(data) / len(data))
else:
    print(-1)
