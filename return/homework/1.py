def month_name(month_index, language):
    MonthsRus = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август',
                 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    MonthsEng = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
                 'september', 'october', 'november', 'december']
    if language == 'ru':
        return MonthsRus[month_index - 1]
    elif language == 'en':
        return MonthsEng[month_index - 1]
