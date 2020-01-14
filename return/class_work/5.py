def number_in_english(number):
    Numbers = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
               'eleven', 'twelve', 'thirteen', 'fourteen', 'fifthteen', 'sixteen', 'seventeen', 'eighteen',
               'nineteen']
    Tens = [None, None, 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    number_1_99 = number % 100
    hundreds = number // 100
    if number == 0:
        return 'zero'
    result = ''
    if hundreds > 0:
        if number_1_99 == 0:
            return Numbers[hundreds] + ' hundred'
        result = Numbers[hundreds] + ' hundred and '
    if number_1_99 < 20:
        return result + Numbers[number_1_99]
    tens = number_1_99 // 10
    digits = number_1_99 % 10
    if digits == 0:
        return result + Tens[tens]
    else:
        return result + Tens[tens] + ' ' + Numbers[digits]

