top_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите новый элемент рейтинга'))
list_updated = False
for i in range(len(top_list)):
    if top_list[i] == new_element:
        top_list.insert(i + 1, new_element)
        list_updated = True
        break

    if top_list[i] < new_element:
        top_list.insert(i , new_element)
        list_updated = True
        break

if list_updated == False:
    top_list.append(new_element)
print(top_list)