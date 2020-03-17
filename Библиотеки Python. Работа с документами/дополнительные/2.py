import xlsxwriter


def export_check(text):
    data = text.split("\n")
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()
    for row, data_row in enumerate(data):
        data_row = data_row.split("\t")
        worksheet.write(row, 0, data_row[0])
        worksheet.write(row, 1, float(data_row[1]))
        worksheet.write(row, 2, int(data_row[2]))
        worksheet.write(row, 3, f'=B{row + 1}*C{row + 1}')

    row += 1
    worksheet.write(row, 0, 'Итого')
    worksheet.write(row, 3, f'=SUM(D1:D{len(data)})')

    workbook.close()
