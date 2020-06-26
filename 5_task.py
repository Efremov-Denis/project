with open('numbers.txt', 'w+', encoding='utf-8') as f:
    f.write('1 2 3')
    f.seek (0)
    content = f.read()
    sumlist = []
    for num in content.split():
        num = int(num)
        sumlist.append(num)
    sum = 0
    for i in range(len(sumlist)):
        sum += sumlist[i]
    print(sum)