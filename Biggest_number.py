number = int(input('Введите целое положительное число'))
result = 0
while number > 0:
	remainder = number % 10
	number // 10
	number = number // 10
	if remainder > result:
		result = remainder
print(result)