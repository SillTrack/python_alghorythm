def even_not_even(number, even=0, odd=0):
	if number == 0:
		return even, odd
	else:
		current_n = number % 10
		number //= 10
		if current_n % 2 == 0:
			even += 1
		else:
			odd += 1
		return even_not_even(number, even, odd)


try:
	numb = int(input('Введите число для подсчета четных и нечетных цифр: '))
	print(f"Количество четных и нечетных чисел в числе: {even_not_even(numb)}")
except ValueError:
	print('Заместо числа была введена строка. Попробуйте ещё раз.')
