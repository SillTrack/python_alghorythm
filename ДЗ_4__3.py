"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""

from timeit import Timer, timeit
import cProfile as CP


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


print('profile with timer:')
t1 = Timer("revers_1(1403)", "from __main__ import revers_1")
print("revers_1(1403) was completed in", t1.timeit(number=1), "seconds")
t1 = Timer("revers_2(1403)", "from __main__ import revers_2")
print("revers_2(1403) was completed in", t1.timeit(number=1), "seconds")
t1 = Timer("revers_3(1403)", "from __main__ import revers_3")
print("revers_3(1403) was completed in", t1.timeit(number=1), "seconds")
t1 = Timer("recursive_reverse(1403)", "from __main__ import recursive_reverse")
print("recursive_reverse(1403) was completed in", t1.timeit(number=1), "seconds")
print("profile with cProfile")
CP.run("main()")
# как и ожидалось решение reverse_3 через встроенные ффункции оказалось самым быстрым ( через срез )


    