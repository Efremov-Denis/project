def MyDegree (x, y):
	x = 2
	y = -2
	result = x
	counter = 1
	while counter < abs(y):
		counter += 1
		result *= x
	return 1 / result
phrase = 'отрицательная степень: '
print(phrase, MyDegree(2, -2))