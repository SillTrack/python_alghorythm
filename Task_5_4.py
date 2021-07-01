from timeit import default_timer
from collections import OrderedDict

some_dict = {}  
some_ordered_dict = OrderedDict()  
n = 10 ** 7  


def time_decorator(some_func):
    def wrapper(*args, **kwargs):
        start = default_timer()
        result = some_func(*args, **kwargs)
        print(f'Время выполенения функции {some_func.__name__} '
              f'составило {default_timer() - start}. ')

        return result

    return wrapper


@time_decorator
def fill_dict(dct, num):
    for i in range(num):
        dct[i] = i


@time_decorator
def fill_ordered_dict(dct, num):
    for i in range(num):
        some_ordered_dict[i] = i


@time_decorator
def change_dict(dct):
    for i in range(1000000):
        dct.pop(i) 
    for j in range(1000001, 2000002):
        dct[j] = 'fill'  
    for k, v in dct.items():
        dct[k] = 'some value' 

@time_decorator
def change_ordered_dict(dct):
    for i in range(1000000):
        dct.pop(i) 
    for j in range(1000001, 2000002):
        dct[j] = 'fill' 
    for k, v in dct.items():
        dct[k] = 'some value'  


fill_dict(some_dict, n)
fill_ordered_dict(some_ordered_dict, n)

change_dict(some_dict)
change_ordered_dict(some_ordered_dict)

NEW_DICT = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)
NEW_DICT.move_to_end('b', last=True) 
print(NEW_DICT)
NEW_DICT.popitem(last=True) 
print(NEW_DICT)
