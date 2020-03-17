import xlsxwriter


def export_check(text):
    data = text.split("---")

    workbook = xlsxwriter.Workbook('res.xlsx')
    for check in data:
        res = {}
        worksheet = workbook.add_worksheet()
        for data_row in check.split("\n"):
            if not data_row.strip():
                continue
            goods, price, count = data_row.strip().split("\t")
            price = float(price)
            count = int(count)
            res[(goods, price)] = res.get((goods, price), 0) + count
        for row, data_row in enumerate(sorted(res.keys(), key=lambda x: x[0])):
            worksheet.write(row, 0, data_row[0])
            worksheet.write(row, 1, data_row[1])
            worksheet.write(row, 2, res[data_row])
            worksheet.write(row, 3, f'=B{row + 1}*C{row + 1}')

        row += 1
        worksheet.write(row, 0, "Итого")
        worksheet.write(row, 3, f'=SUM(D1:D{len(res)})')

    workbook.close()
