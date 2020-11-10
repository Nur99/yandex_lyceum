import csv

percent = float(input())
result = []
with open('vps.csv') as in_file:
    reader = csv.reader(in_file)
    for i, row in enumerate(reader):
        if i > 0:
            line = row[0].split(';')
            if float(line[-2]) >= percent:
                result.append(line[0])
print(*result, sep='\n')
