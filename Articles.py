n = int(input('Введите количество товаров'))

main_list = []

for i in range(1, n+1):
    list_titles = input('Введите названия характеристик').split(' ')
    list_values = input('Введите характеристики товара').split(' ')
    my_dict = dict(zip(list_titles, list_values))
    main_list.append((i,my_dict))
    print(main_list)

result_dict = dict()

for cortege in main_list:
    current_dict = cortege[1]
    for key in current_dict.keys():
        value = current_dict[key]
        if key in result_dict:
            if value not in result_dict[key]:
                result_dict[key].append(value)
        else:
            result_dict[key] = [value]

print(result_dict)