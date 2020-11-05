import csv


def get_surname(student):
    return student["user_name"].split()[3]


with open("rez.csv", "r", encoding='utf8') as infile:
    students = csv.DictReader(infile, delimiter=",", quotechar='"')
    school, clas = list(map(int, input().split()))
    target = []
    for student in students:
        login = student["login"].split("-")
        s_school, s_class = int(login[2]), int(login[3])
        if school == s_school and clas == s_class:
            target += [student]
    target = list(sorted(target, key=lambda student: get_surname(student),
                         reverse=True))
    target = list(sorted(target, key=lambda student: int(student["Score"]),
                         reverse=True))
    for student in target:
        login = get_surname(student)
        score = student["Score"]
        print(login, score)
