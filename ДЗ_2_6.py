import random as r

def function(try_count = 10, number = int(r.random() * 100)):

    if try_count == 0:
        print('Попытки закончились, загаданное число -', number)
    print('Загадано число от 1 до 100. Попробуйте угадать его! У вас осталось', try_count, ' попыток!', end= '\n')
    user_number = int(input())
    if user_number < number:
        print('Ваше число меньше загаданного')
        function(try_count - 1, number)
    elif user_number > number:
        print('Ваше число больше загаданного')
        function(try_count - 1, number)
    else:
        print('Вы угадали!')
        return


function()