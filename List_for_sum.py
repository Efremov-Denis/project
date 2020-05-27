while True:
	numberslist = input('Введите числа, разделяя их пробелами').split()
	sum = 0
	ending_symbol = 'a'
	for elem in numberslist:
		if elem != ending_symbol:
			elem = int(elem)
			sum += elem
	print(sum)
	if numberslist[0] == ending_symbol:
		break
print('Конец программы')