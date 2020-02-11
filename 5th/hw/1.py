def shift_letter(letter, shift):
    letter_in_alphabet = ord(letter) - ord('а')
    alphabetLength = ord('я') - ord('а') + 1
    shifted_letter_in_alphabet = (letter_in_alphabet + shift) % alphabetLength
    return chr(ord('а') + shifted_letter_in_alphabet)


def encrypt_caesar(msg, shift=3):
    result = ''
    for letter in msg:
        if 'а' <= letter.lower() <= 'я':
            if letter.islower():
                result += shift_letter(letter, shift)
            else:
                result += shift_letter(letter, shift).upper()
        else:
            result += letter
    return result


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -shift)
