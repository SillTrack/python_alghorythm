# решение перебором каждого элемента с каждым
def look_for_min(user_list):
    l = len(user_list)
    min = user_list[0]
    for j in range(0,l):
        for i in range(0,l):
            if user_list[j] > user_list[i]:
                if min > user_list[i]:
                    min = user_list[i]
    return min


def look_for_min_n(user_list):
    min = user_list[0]
    for i in range(1, len(user_list)):
        if user_list[i] < min:
            min = user_list[i]
    return min


example = [1, 3, 5, -1, 23, 0]
# a = len(example);
# print(a);
result = look_for_min(example)
print(result)
# решение поиском минимального значения списка
result = look_for_min_n(example)
print(result)
