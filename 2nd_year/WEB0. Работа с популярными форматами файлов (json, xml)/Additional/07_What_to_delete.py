import os
from os.path import isfile, getsize

path = '.'


def good_human_read_format(size):
    values = ['Б', 'КБ', 'МБ', 'ГБ']
    num = 0
    while size >= 1024:
        size /= 1024
        num += 1
    return f"{round(size)}{values[num]}"


def get_full_size(path):
    if isfile(path):
        return getsize(path)
    else:
        return sum([get_full_size(f'{path}/{f}') for f in os.listdir(path)])


info = [(name, get_full_size(f'{path}/{name}')) for name in os.listdir(path)]
info.sort(key=lambda x: x[1], reverse=True)
for data in info[:10]:
    print(f'{data[0]:<50} - {good_human_read_format(data[1]):>5}')
