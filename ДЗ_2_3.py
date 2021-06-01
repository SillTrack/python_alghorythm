def swap(number, swaped_number = ''):
    if number < 10:
        swaped_number += str(number)
        print('Перевернутое число:', swaped_number)
        return
    swaped_number += str(number % 10)
    number //= 10
    swap(number, swaped_number)


swap(1230)
swap(6632)