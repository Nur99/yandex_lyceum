import csv
import sys

headers = ['nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia']
data = [line.rstrip().split('\t') for line in sys.stdin]
with open('plantis.csv', 'w', encoding='utf8', newline='') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    writer.writerow(headers)
    writer.writerows(data)