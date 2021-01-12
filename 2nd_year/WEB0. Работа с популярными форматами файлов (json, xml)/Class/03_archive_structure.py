from zipfile import ZipFile

with ZipFile('input.zip') as myzip:
    for z in myzip.filelist:
        name = z.filename
        # print(name)
        if name[-1] == '/':  # каталог
            print('  ' * (name.count('/') - 1) + z.orig_filename.split('/')[-2])
        else:
            print('  ' * (name.count('/')) + z.orig_filename.split('/')[-1])