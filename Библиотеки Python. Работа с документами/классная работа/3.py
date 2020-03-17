from docxtpl import DocxTemplate


def create_training_sheet(name, sub, docname, *students):
    doc = DocxTemplate(docname)
    students = sorted(students, key=lambda x: x[0])
    a = list()
    for i in range(len(students)):
        a.append({
            'num': i + 1,
            'fio': students[i][0],
            'mark': students[i][1]
        })
    context = {
        'class_name': name,
        'subject_name': sub,
        'marks': a
    }
    doc.render(context)
    doc.save("res.docx")
