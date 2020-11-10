import csv

with open('alpha_oriona.csv') as file:
    reader = csv.DictReader(file, delimiter=';')
    data = [(int(x['luminosity']), x['date'], x['time']) for x in reader]
max_l = length = index = 0
temp = [x[0] for x in data]

for i in range(1, len(data)):
    if temp[i] <= temp[i - 1]:
        length += 1
    else:
        if length > max_l:
            max_l = length
            index = i
        length = 0
if length > max_l:
    max_l = length
    index = len(data)
index -= max_l + 1

with open('result.txt', 'w') as res:
    print(str(max_l + 1), file=res)
    print(' '.join([data[index][1], data[index][2]]), file=res)