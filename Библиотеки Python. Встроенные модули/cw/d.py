import datetime as dt
n = dt.datetime.now()
s = dt.timedelta(days=int(input()))
a = str((n + s).date()).split('-')
print(int(a[2]), int(a[1]))
