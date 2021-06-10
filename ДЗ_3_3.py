import hashlib


my_set = set()
my_str = 'rose'
for i in range(len(my_str)):
    for j in range(i + 1, len(my_str) + 1):
        if my_str[i:j] != my_str:
            my_set.add(hashlib.sha256(my_str[i:j].encode()).hexdigest())
            print(my_str[i:j], end=' ')


print(f'\n{my_set}')
print(f'Количество элементов в множестве: {len(my_set)}')