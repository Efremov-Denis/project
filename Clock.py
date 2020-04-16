fulltime = int(input('Введите количество секунд'))
hourses = fulltime // 3600
minutes = (fulltime % 3600) // 60
seconds = (fulltime % 3600) % 60
print(f"прошло: {hourses}: {minutes}: {seconds}")