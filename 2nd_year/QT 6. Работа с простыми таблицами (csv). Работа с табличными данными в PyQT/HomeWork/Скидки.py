import csv

with open('wares.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        if int(row['New price']) - int(row['Old price']) < 0:
            print(row['Name'])
