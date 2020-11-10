import csv

sh, k = map(int, input().split())
with open('rez.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    last_name = []
    for index, row in enumerate(reader):
        if row[2] != "login":
            fio = row[2].split('-')
            if int(fio[2]) == sh and int(fio[3]) == k:
                name = row[1].split()
                last_name.append((int(row[7]), name[-2]))
    last_name = sorted(last_name, reverse=True)
    f = open('output.txt', 'w')
    for i in range(len(last_name)):
        print(last_name[i][1], last_name[i][0])
    f.close()