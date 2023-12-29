first_day_result = int(input('Сколько километров спортсмен пробежал в первый день?'))
general_result = int(input('Введите результат, который нужно достигнуть'))
final_day = 1
while first_day_result < general_result:
	first_day_result = first_day_result + first_day_result * 0.1
	final_day = final_day + 1
print(final_day)