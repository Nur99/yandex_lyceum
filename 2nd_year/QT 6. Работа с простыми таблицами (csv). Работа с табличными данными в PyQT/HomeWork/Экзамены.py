import csv
import sys

n, m = map(int, input().split())
lines = map(str.rstrip, sys.stdin.readlines())
data = [['Фамилия', 'имя', 'результат 1', 'результат 2', 'результат 3', 'сумма']]
for line in lines:
    last_name, first_name, r_1, r_2, r_3 = line.split()
    sum_ = int(r_1) + int(r_2) + int(r_3)
    if sum_ >= n and all([int(r_1) >= m, int(r_2) >= m, int(r_3) >= m]):
        data.append([last_name, first_name, r_1, r_2, r_3, str(sum_)])
with open('exam.csv', 'w', encoding='utf8', newline='') as out_file:
    writer = csv.writer(out_file, delimiter=';')
    writer.writerows(data)