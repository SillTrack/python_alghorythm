def function(number_in_row = 1, current_symbol = 32):
    if current_symbol <= 127:
        if number_in_row < 10:
            print(current_symbol, '-', chr(current_symbol), end= ' ')
            function(number_in_row + 1, current_symbol + 1)
        else:
            print(current_symbol, '-', chr(current_symbol),)
            number_in_row = 1
            function(number_in_row, current_symbol + 1)
    else:
        return



function()