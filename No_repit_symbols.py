list = [2, 1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 2]
new_list = [elem for elem in list if list.count(elem) == 1]
print(new_list)