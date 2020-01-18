messages = None


def print_without_duplicates(message):
    global messages
    if message != messages:
        messages = message
        print(message)
