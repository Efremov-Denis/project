number = int(input('enter an integer'))
max = 0
result = 0
while number > 0:
    max = number % 10
    number // 10
    number //= 10
    if result < max:
        result = max
print(result)