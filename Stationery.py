class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')

class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')

class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')

stationary = Stationery('abc')
pen = Pen('abc')
pencil = Pencil('abc')
handle = Handle('abc')

stationary.draw()
pen.draw()
pencil.draw()
handle.draw()