import random as r
import time as t
import sys as s


def memorize(func):
    def g(n):
        time_1 = t.time()
        func(n)
        time_2 = t.time()
        delta = time_2 - time_1
        print('Время заполнения - ', delta)
    return g


@memorize
def list_filling(n):
    my_list = []
    for i in range(n):
        my_list.append(int(r.randint(0, i)*10))
    return my_list


def list_filling_without_dec(n):
    my_list = []
    for i in range(n):
        my_list.append(int(r.randint(0, i)*10))
    return my_list


def dict_filling_without_memorize(n):
    my_dict = {}
    for i in range(n):
        my_dict.update({i: (int(r.randint(0, i)*10))})
    return my_dict


@memorize
def dict_filling(n):
    my_dict = {}
    for i in range(n):
        my_dict.update({i: (int(r.randint(0, i)*10))})
    return my_dict


@memorize
def list_functions(n):
    current_list = list_filling_without_dec(n)
    current_list.clear()


@memorize
def dict_function(n):
    current_dict = dict_filling_without_memorize(n)
    current_dict.clear()


print('Время заполнения списка')
list_filling(10000000)
print('Время заполнения словаря')
dict_filling(10000000)
# Время заполнения списка меньше времени заполнения словаря
print('врем очистки словаря')
dict_function(1000000)
print('время очистки списка')
list_functions(1000000)
# Время очистки списка меньше времени очистки словаря
print('размер списка:', s.getsizeof(list_filling_without_dec(10000000)))
print('размер словаря с тем же количеством элементов:', s.getsizeof(dict_filling_without_memorize(10000000)))
