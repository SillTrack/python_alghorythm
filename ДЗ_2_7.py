def function(row_length, current_length=1, sum_of_row=0):
    if current_length <= row_length:
        function(row_length, current_length + 1, sum_of_row + current_length)
    else:
        print('Посчитано программой: ', sum_of_row)


number_of_elemnts = int(input('Введите количество элементов: '))
function(number_of_elemnts)
print('Подсчет по формуле: ', number_of_elemnts * (number_of_elemnts + 1) / 2)

