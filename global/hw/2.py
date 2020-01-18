savedName = None
savedVacationDates = None


def setup_profile(name, vacationDates):
    global savedName, savedVacationDates
    savedName = name
    savedVacationDates = vacationDates


def print_application_for_leave():
    print("Заявление на отпуск в период " +
          savedVacationDates + ". " + savedName)


def print_holiday_money_claim(amount):
    print("Прошу выплатить " + amount + " отпускных денег. " + savedName)


def print_attorney_letter(toWhom):
    print("На время отпуска в период " + savedVacationDates +
          " моим заместителем назначается " + toWhom + ". " + savedName)
