list = [3, 2, 3, 7, 6]

new_list = [list[i] for i in range(1,len(list)) if list[i] > list[i-1]]
print(new_list)