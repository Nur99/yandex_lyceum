import csv

summ = 1000

with open('wares.csv', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    rows = [(r[0], int(r[1])) for r in reader]

rows.sort(key=lambda x: x[1])

if rows[0][1] > summ:
    print('error')

res = []

while rows and summ >= rows[0][1]:
    count = summ // rows[0][1]
    if count > 10:
        count = 10

    summ -= count * rows[0][1]
    res = res + ([rows[0][0]] * count)
    rows.pop(0)

print(", ".join(res))
