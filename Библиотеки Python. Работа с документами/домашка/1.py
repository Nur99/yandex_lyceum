import xlsxwriter
 
workbook = xlsxwriter.Workbook('диаграммы.xlsx')
worksheet = workbook.add_worksheet()
 
data1 = ['Питание', 'Развлечения', 'Учеба', 'Лечение', 'Прочее']
data2 = [1200, 1500, 300, 100, 670]
worksheet.write_column('A1', data1)
worksheet.write_column('B1', data2) 

chart = workbook.add_chart({'type': 'pie'})
chart.add_series({'values': '=Sheet1!A1:B5'})
worksheet.insert_chart('C3', chart)
workbook.close()
