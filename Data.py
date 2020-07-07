class Data:

    def __init__(self, date = 'day:month:year'):
        self.date = date

    @classmethod
    def DateNumber(cls, date):
        cls.date = date
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
        return day, month, year

    @staticmethod
    def Validation(day, month, year):
        if day > 31:
            print("incorrect day")
        if month > 12:
            print("incorrect month")

my_date = Data('31:15:2020')

x = my_date.DateNumber('31:15:2020')

print(x)
Data.Validation(x[0], x[1], x[2])