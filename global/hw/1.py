def translate(text):
    global translatedText
    letters = ''
    valid = "бвгджзйклмнпрстфхцчшщъь "
    for t in text:
        if t.lower() in valid:
            letters += t
    translatedText = ' '.join(letters.split())
