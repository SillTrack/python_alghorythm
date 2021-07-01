import collections
import functools


def calc():
    nums = collections.defaultdict(list)
    for d in range (2):
        n = input(f'Введите {d+1}-e натуральное шестнадцатиричное число: ')
        nums[f'{d+1}-{n}'] = list(n)
    print(nums)
    
    result = sum([int(''.join(i), 16) for i in nums.values()])
    print(result)
    print('Сумма', list('%X' % result))
    multiply_result = functools.reduce(lambda a, b: a * b,
                            [int(''.join(i),16) for i in nums.values()])
    print('Произведение: ', list ('%X' % multiply_result))

calc()