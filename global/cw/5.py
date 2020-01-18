clientName = None


def polite_input(question):
    global clientName
    if not clientName:
        print('Как вас зовут?')
        clientName = input()
    print(clientName + ', ' + question)
    return input()
