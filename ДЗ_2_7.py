def function(row_length, current_length = 1, summ_of_row = 0):
    if current_length <= row_length:
        function(row_length, current_length + 1, summ_of_row + current_length)
    else:
        print('Подсчет по формуле: ', row_length*(row_length+1)/2)
        print('Посчитано программой: ', summ_of_row)


function(3)