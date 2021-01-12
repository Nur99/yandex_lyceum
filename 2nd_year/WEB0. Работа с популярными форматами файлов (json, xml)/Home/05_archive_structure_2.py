from zipfile import ZipFile


def good_human_read_format(size):
    values = ['Б', 'КБ', 'МБ', 'ГБ']
    num = 0
    while size >= 1024:
        size /= 1024
        num += 1
    return f"{round(size)}{values[num]}"


with ZipFile('input.zip') as myzip:
    for file in myzip.filelist:
        name = file.filename
        if name[-1] == '/':  # каталог
            print('  ' * (name.count('/') - 1) + file.orig_filename.split('/')[-2])
        else:
            print(f"{'  ' * (name.count('/'))}{file.orig_filename.split('/')[-1]} "
                  f"{good_human_read_format(file.file_size)}")
