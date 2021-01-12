def human_read_format(size):
    values = ['Б', 'КБ', 'МБ', 'ГБ']
    num = 0
    while size >= 1024:
        size /= 1024
        num += 1
    return f"{round(size)}{values[num]}"


print(human_read_format(1500000000))