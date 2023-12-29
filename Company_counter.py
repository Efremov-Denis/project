charges = int(input('Введите сумму издержек'))
effect = int(input('Введите сумму выручки'))
profit = effect - charges
if profit > 0:
	profitability = profit / effect * 100
	print('Ваша деятельность приносит прибыль')
	print('Рентабельность выручки составляет ', profitability, ' %.')
if profit == 0:
	print('Ваша деятельность не приносит прибыль')
if profit < 0:
	print('Ваша деятельность убыточна')
workers = int(input('Сколько у вас сотрудников?'))
one_worker_profit = profit // workers
print('Прибыль в расчете на одного сотрудника составляет ', one_worker_profit, ' рублей')