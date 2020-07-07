from abc import ABC, abstractmethod

class MyAbstractClass(ABC):

    @abstractmethod
    def my_method_1(self):
        pass

class Dress(MyAbstractClass):

    def __init__(self, V, H):
        self.V = V
        self. H = H

    @property
    def my_method(self):
        return f"Параметры, переданные в класс:" \
            f" {self.V}, {self.H}"

    def my_method_1(self):
        print("Метод my_method_1()")

    def MaterialConsumptiontoCoat(self, V):
        return V/6.5 + 0.5

    def MaterialConsumptiontoSuit(self, H):
        return 2 * H + 0.3

dress = Dress(38, 82)
print(dress.MaterialConsumptiontoCoat(38))
print(dress.MaterialConsumptiontoSuit(82))
print(f'общий расход ткани составляет {(dress.MaterialConsumptiontoCoat(38) + dress.MaterialConsumptiontoSuit(82)):.1f}')
dress.my_method_1()
print(dress.my_method)