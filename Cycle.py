from itertools import cycle

с = 0
for el in cycle([5, 6, 7]):
    if с > 10:
        break
    print(el)
    с += 1