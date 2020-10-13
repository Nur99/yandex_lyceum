import sys

data = open('data.txt', 'rb').read()
count = len(data)

print("          %s\n" % "".join(("%0.2x " % i for i in range(16))))

for i in range(count // 16 + 1):
    part = data[i * 16: i * 16 + 16]
    if part:
        printable = "".join((chr(p) if chr(p).isprintable() else "." for p in part))
        print(("%0.5x0    " % i) +
              "".join(("%0.2x " % p for p in part)) +
              " " * ((16 - len(part)) * 3 + 4) + printable)
