from zipfile import ZipFile
from json import loads

n = 0

with ZipFile('input.zip') as myzip:
    for z in myzip.filelist:
        if '.json' in z.filename:
            with myzip.open(z.filename, 'r') as file:
                data = file.read().decode('utf8')
                d = loads(data)
                if d['city'] == 'Москва':
                    n += 1

print(n)
