data = open('prices.txt', 'rt', encoding='utf8').read().strip().split('\n')

s = 0
for d in data:
    if not d:
        continue
    name, count, price = d.split('\t')
    count = int(count)
    price = float(price)
    s += price * count

print("%0.2f" % s)
