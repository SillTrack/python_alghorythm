def even_not_even(number, even = 0, n_even = 0):
	flag = 0
	if number < 10 and (number % 10) == 0:
		even += 1
		flag = 1
	elif number < 10 and (number % 10) == 1:
		n_even += 1  
		flag = 1
	if flag == 1:
		print ([even, n_even])
		return
	digit = number % 10
	if (digit % 2) == 0:
		even += 1
		number //= 10
		even_not_even(number, even, n_even)
	else:
		n_even += 1
		number //= 10
		even_not_even(number, number, n_even)
    

even_not_even(142)


