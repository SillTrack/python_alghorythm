import memory_profiler


def decor(func):
    def wrapper(x, y):
        m1 = memory_profiler.memory_usage()
        res = func(x, y)
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


@decor
def my_func(x, y):
    iterator = 1
    base = x
    collector = []
    while iterator < abs(y):
        x *= base
        collector.append(x)
        iterator += 1
    return collector


@decor
def my_func_yiedlded(x, y):
    iterator = 1
    base = x
    collector = list(x)
    while iterator < abs(y):
        x *= base
        collector.append(x)
        iterator += 1
    yield collector


while True:
    try:
        number_base = int(input('Введите число x: '))
        number_exponent = int(input('Введите показатель степени y (отрицательное): '))
    except ValueError:
        print('Введите число!')
    if number_base > 0 > number_exponent:
        break
while True:
    try:
        flag = int(input('Введите 1 если программа должна быть выполнена через my_fync(x, y), 0 - иначе: '))
    except ValueError:
        print('Введите число!')
        continue
    if flag == 0 or flag == 1:
        break
if flag == 1:
    powered_x, mem_dif = my_func(number_base, number_exponent)
    print('Программа выполнена через my_fync(x, y), паммяти потрачено:', mem_dif)
else:
    powered_x, mem_dif = my_func_yiedlded(number_base, number_exponent)
    print('Программа выполнена через my_fync_yield(x, y), паммяти потрачено:', mem_dif)

# Введите число x: 10
# Введите показатель степени y (отрицательное): -10000
# Введите 1 если программа должна быть выполнена через my_fync(x, y), 0 - иначе: 1
# Программа выполнена через my_fync(x, y), паммяти потрачено: 23.6953125

# Введите число x: 10
# Введите показатель степени y (отрицательное): -10000
# Введите 1 если программа должна быть выполнена через my_fync(x, y), 0 - иначе: 0
# Программа выполнена через my_fync_yield(x, y), паммяти потрачено: 0.0078125

# при использовании функции без генератора, затрачиваемая память практически в 1000 ращ больше чем при
# использовании генератора
