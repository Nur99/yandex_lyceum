def print_document(document):
    for page in document:
        if page.startswith('Секретно'):
            print("Дальнейшие материалы засекречены")
            return
        print(page)
    print("Напечатано без купюр")
