def division (number1, number2):
	try:
		number1 = int(input('Введите первое число'))
		number2 = int(input('Введите второе число'))
		result = number1 / number2
	except ZeroDivisionError:
		return
	return int(result)
print(division(4, 2))