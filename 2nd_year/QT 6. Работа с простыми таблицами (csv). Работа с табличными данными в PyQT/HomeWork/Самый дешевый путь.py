import csv

with open('input.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    rows = [r for r in reader]
    A, B = rows[-1][:2]

    prices = {}
    for f, t, p in rows[:-1]:
        if f not in prices:
            prices[f] = {t: int(p)}
        else:
            prices[f][t] = int(p)

    variants = []
    for dest, price in prices[A].items():
        if dest == B:  # Прямой
            variants.append(('%s %s' % (A, B), price))
        elif B in prices[dest]:  # C пересадкой
            variants.append(('%s %s %s' % (A, dest, B), price + prices[dest][B]))

    variants.sort(key=lambda x: x[1])
    print(variants[0][0])
