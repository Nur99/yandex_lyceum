def translation(s, k):
    k += 1
    rez = ''
    for i in s:
        c = s.find(i)
        key = c + k
        if key > len(s):
            key = key % len(s)
        elif key < 0:
            key = key % len(s)
        rez += s[key - 1]
    print(rez)
  
  
def translation2(s, k):
    k = len(s) - k + 1
    rez = ''
    for i in s:
        c = s.find(i)
        key = c + k
        if key > len(s):
            key = key % len(s)
        elif key < 0:
            key = key % len(s)
        rez += s[key - 1]
    print(rez)
 

s = input()
k = int(input())
translation(s, k)
print(s)
translation2(s, k)
