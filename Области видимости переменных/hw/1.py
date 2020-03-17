def from_string_to_list(string, container):
    for number in string.split():
        value = int(number)
        container.append(value)
