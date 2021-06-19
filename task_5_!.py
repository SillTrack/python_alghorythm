from statistics import mean
from collections import defaultdict


number = int(input('Введите количество компаний'))

my_dict = defaultdict(int)

for i in range(number):
    company = input('Введите название предприятия: ')
    profit = input('Введите прибыль за каждый квартал для данной компании через пробел (4 кваратала)')
    my_dict[company] = mean([int(el) for el in profit.split(' ')])

average_profit = round(mean(my_dict.values()), 3)
profit(f'Среднеговодовая прибыль для всех предприятий: {average_profit}.')

print(f'Предпрития с прибылью, ниже среднеговой: '
       f"{', '.join([el for el in my_dict.keys() if my_dict[el] < average_profit])}.")

print(f'Предпрития с прибылью, выше среднеговой: '
       f"{', '.join([el for el in my_dict.keys() if my_dict[el] > average_profit])}.")