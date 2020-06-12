fulltime = int(input('Введите количество секунд'))
hours = fulltime // 3600
minutes = (fulltime % 3600) // 60
seconds = (fulltime % 3600) % 60
print(f"прошло: {hours:02}: {minutes:02}: {seconds:02}")