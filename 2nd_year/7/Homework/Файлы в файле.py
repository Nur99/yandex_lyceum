def measures(number, unit):
    volumes = {'b': 1, 'Kb': 2 ** 10, 'Mb': 2 ** 20, 'Gb': 2 ** 30}
    return number * volumes[unit]


def convert(number):
    if number < 2 ** 10:
        return f'{number} b'
    if number < 2 ** 20:
        return f'{round(number / 2 ** 10)} Kb'
    if number < 2 ** 30:
        return f'{round(number / 2 ** 20)} Mb'
    return f'{round(number / 2 ** 30)} Gb'


with open('input.txt') as in_file:
    data = {}
    for line in map(str.rstrip, in_file.readlines()):
        file_name, volume, units = line.split()
        name, extension = file_name.split('.')
        if extension not in data:
            data[extension] = [[name], measures(int(volume), units)]
        else:
            data[extension][0].append(name)
            data[extension][1] += measures(int(volume), units)
data = {key: ['\n'.join([f'{name}.{key}'
                         for name in sorted(data[key][0])]), data[key][1]]
        for key in sorted(data.keys())}

with open('output.txt', 'w') as out_file:
    for item in data.values():
        print(item[0], file=out_file)
        print('-' * 10, file=out_file)
        print(f'Summary: {convert(item[1])}', file=out_file)
        print(file=out_file)
