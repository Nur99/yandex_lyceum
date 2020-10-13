def palindrome():
    with open('input.dat', 'rb') as input:
        data = input.read()
        return data == data[::-1]
