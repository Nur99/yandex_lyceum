import json

f = open("scoring.json")
s = json.load(f)
print(s['scoring'][0])
sum_all = 0
for i in range(len(s["scoring"])):
    p = s["scoring"][i]["points"]
    k = 0
    n = len(s["scoring"][i]["required_tests"])
    for j in range(n):
        verd = input()
        if verd == "ok":
            k += 1
    sum_all += k * p // n
print(sum_all)