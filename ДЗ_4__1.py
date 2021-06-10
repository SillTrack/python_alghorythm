from timeit import Timer

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    return [index for index,element in enumerate(nums) if not element%2]
# Воспользовался тернарным оператором для ускорения кода.
# Функция enumerate использована для однозначного определения индекса при наличии повторяющихся элементов 


t1 = Timer('func_1(nums=[1, 2, 3, 4, 5, 6])', 'from __main__ import func_1')
print("list of idex of even numbers ", t1.timeit(number=10000000), "seconds")
t2 = Timer('func_2(nums=[1, 2, 3, 4, 5, 6])', 'from __main__ import func_2')
print("list of idex of even numbers with my program", t1.timeit(number=10000000), "seconds")


