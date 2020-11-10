import csv

district = input()
start_year, end_year = input().rstrip().split()

with open('salary.csv', encoding='utf8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';', quotechar='"')
    result = [{'Субъект': item['Субъект'],
               start_year: item[start_year],
               end_year: item[end_year]} for item in reader
              if item['Федеральный округ'] == district and
              (int(item[end_year]) -
               int(item[start_year])) / int(item[start_year]) < 0.04]

if result:
    with open('out_file.csv', 'w', newline='') as out_file:
        writer = csv.DictWriter(
            out_file, fieldnames=list(result[0].keys()), delimiter=';')
        writer.writeheader()
        for d in result:
            writer.writerow(d)
else:
    with open('out_file.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file).writerow('')
