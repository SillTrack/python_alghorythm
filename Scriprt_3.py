from functools import reduce
from sys import getsizeof
from numpy import array


def my_func(prev_el, el):
    return prev_el * el


new_list = [i for i in range(100, 1001, 2)]
print(getsizeof(new_list))
print(new_list)
print(reduce(my_func, new_list))


new_list_v2 = array([i for i in range(100, 1001, 2)])
print(getsizeof(new_list_v2))

# Как и ожидалось, использование array для большого количества данных имеет преимущество в памяти
# по сравнению с обычными коллекциями
