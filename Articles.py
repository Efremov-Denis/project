n = int(input())

main_list = []

for i in range(1, n+1):
	list_titles = input('Введите названия характеристик').split(' ')
	list_values = input('Введите характеристики товара').split(' ')
	my_dict = dict(zip(list_titles, list_values))
	main_list.append((i,my_dict))
	print(main_list)