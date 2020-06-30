class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def ShowSpeed(self):
        print('текущая скорость автомобиля - ', 90)

    def go(self):
        print('автомобиль поехал')

    def stop(self):
        print('автомобиль остановлен')

    def turn(self, direction):
        if direction == 0:
            print('автомобиль едет назад')
        elif direction == 1:
            print('автомобиль едет направо')
        else:
            print('автомобиль едет налево')

class TownCar(Car):

    def ShowSpeed(self, speed):
        print('текущая скорость автомобиля - ', 70)
        if speed > 60:
            print('вы превысили скорость')

class SportCar(Car):
	pass

class WorkCar(Car):

    def ShowSpeed(self, speed):
        print('текущая скорость автомобиля - ', 50)
        if speed > 40:
            print('вы превысили скорость')

class PoliceCar(Car):
	pass

car_c = Car(60, 'красного', 'BMW')
car_t = TownCar(70, 'черного', 'городская машина')
car_w = WorkCar(50, 'серого', 'такой грузовик, вот')
car_s = SportCar(50, 'оранжевого', 'гонка')
car_p = PoliceCar(100, 'черного', ' BMW', True)
print(f'Это - {car_c.name}, {car_c.color} цвета')
print(f'Это - {car_t.name}, {car_t.color} цвета')
print(f'Это - {car_w.name}, {car_w.color} цвета')
print(f'Это - {car_s.name}, {car_s.color} цвета')
print(f'Это полицейская машина - {car_p.name}, {car_p.color} цвета {car_p.is_police}')
car_c.ShowSpeed()
car_c.go()
car_c.stop()
car_c.turn(0)
car_t.ShowSpeed(70)
car_w.ShowSpeed(50)