import csv
import xlrd

workbook = xlrd.open_workbook("data.xlsx")
sheet = workbook.sheet_by_index(0)

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for rownum in range(sheet.nrows):
        writer.writerow(sheet.row_values(rownum))
