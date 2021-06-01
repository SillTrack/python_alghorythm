def calculator():
    while True:
        sign = input('Введите знаки "/", "*", "+", "-" для действий между числами или "0" для выхода из программы: ')
        if sign == '/' or sign == '*' or sign == '+' or sign == '-' or sign == '0':
            break
    if sign == '0':
        print('Конец программы!')
        return
    try:
        first_number = int(input('Введите первое число: '))
    except ValueError:
        print('Вы ввели не число');
        calculator()
    try:
        second_number = int(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели не число');
        calculator()
    if sign == '/':
        try:
            result = first_number / second_number
            print('Ответ:', result)
            calculator()
        except ZeroDivisionError:
            print('Ошибка деления на нуль, программа будет запущена с начала!')
            calculator()
    elif sign == '*':
        print('Ответ:', first_number * second_number)
        calculator()
    elif sign == '-':
        print('Ответ:', first_number - second_number)
        calculator()
    elif sign == '+':
        print('Ответ:', first_number + second_number)
        calculator()
    

calculator()