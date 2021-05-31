# Сама задача:
# Имеется хранилище с информацией о компаниях: название и годовая прибыль.
# Для реализации хранилища можно применить любой подход,
# который вы придумаете, например, реализовать словарь.
# Реализуйте поиск трех компаний с наибольшей годовой прибылью.
# Выведите результат.
# Решение_1 Сложность n^2 - квадратичная
max = 0
max_list = []
info = [["name_1", 10000], ["name_2", 20000], ["name_3", 30000],
["name_4", 40000], ["name_5", 50000]]
for el in info:
    if len(max_list) == 3:
        for element in max_list:
            if element < el[1]:
                max_list.append(el[1])
                max_list.remove(element)
                break
    else:
        max_list.append(el[1])

print(max_list)


max_list.clear()


# 2 способ сложность nlogn - линейно - логарифмическая (лучше чем квадратичная)
print("2 cпособ")
for el in info:
    max_list.append(el[1])
max_list.sort()
max_list.reverse()
for i in range(0, 3):
    print(max_list[i])
