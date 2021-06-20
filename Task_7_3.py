import timeit
from random import randint
from statistics import median


def without_sort(lst_obj):
    temp = lst_obj
    left_list = []
    right_list = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                left_list.append(temp[j])
            if temp[i] < temp[j]:
                right_list.append(temp[j])
            if temp[i] == temp[j] and i > j:
                left_list.append(temp[j])
            if temp[i] == temp[j] and i < j:
                right_list.append(temp[j])
        if len(left_list) == len(right_list):
            return temp[i]
        left_list.clear()
        right_list.clear()


def another_way(lst_obj):
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


def gnome_sort(sort_list):
    i = 1
    while i < len(sort_list):
        if not i or sort_list[i - 1] <= sort_list[i]:
            i += 1
        else:
            sort_list[i], sort_list[i - 1] = sort_list[i - 1], sort_list[i]
            i -= 1
    return sort_list


def gnome_median(sort_list):
    return gnome_sort(sort_list)[len(sort_list) // 2]


m = int(input('Введите m: '))
orig_list = [randint(0, 100) for i in range(2 * m + 1)]
print(f'Исходный массив:\n{orig_list}\n')


print(f'Медиана - {median(orig_list[:])}')
print(f'Медиана (без сортировки) - {without_sort(orig_list[:])}')
print(f'Медиана (без сортировки) - {another_way(orig_list[:])}')
print(f'Медиана (с сортировкой) - {gnome_sort(orig_list[:])[m]}')
print(f'Отсортированный массив:\n {gnome_sort(orig_list[:])}')

print(
    timeit.timeit(
        "median(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "without_sort(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "another_way(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "gnome_sort(orig_list[:])",
        globals=globals(),
        number=1000))

