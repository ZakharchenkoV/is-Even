def isEven(numb):
    even_numb = [2, 4, 6, 8, 0]  # В данном случае при наихудшем исходе программа обращается к списку 5 раз (5
    # операций сравнения), в связи с чем для ее выполнения будет потрачено 5мс, что в 5 раз больше, чем в случае с
    # остатком от деления на 2 и сравнении с 0. Минусы данного алгоритма: скорость исполнения, память (список),
    # скорость написания кода.
    if numb % 10 in even_numb:
        return "Even"
    else:
        return "Uneven"


value = int(input())

print(isEven(value))
