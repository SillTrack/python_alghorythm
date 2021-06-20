

import random
import timeit


def sort_1(list_object):
    flag = 1
    while flag:
        flag = 0
        for i in range(len(list_object) - 1):
            if list_object[i] < list_object[i + 1]:
                list_object[i], list_object[i + 1] = list_object[i + 1], list_object[i]
                flag = 1
    return list_object

def sort_2(list_object):
    flag = 1
    counter = 0 
    while flag:
        flag = 0
        for i in range(len(list_object) - counter - 1):
            if list_object[i] < list_object[i + 1]:
                list_object[i], list_object[i + 1] = list_object[i + 1], list_object[i]
                flag = True
        counter += 1
    return list_object


list_object = [random.randint(-100, 100) for i in range(1000)]

print(
    timeit.timeit(
        "sort_1(list_object[:])",
        globals=globals(),
        number=200))
print(
    timeit.timeit(
        "sort_2(list_object[:])",
        globals=globals(),
        number=200))


# для первой сортировки ушло 23.6765809
# для второй - 15.155139799999997
# такой прирост по скорости связан с улучшением алгоритма путем уменьшением количества проходов
# в каждом алгоритме. На малых количествах проходов не сильная разница, но при увеличении прохоов до сотни
# прирост скорости около 8.5 секунд
