class Cell:

    def __init__(self, faveolus_number):
        self.faveolus_number = faveolus_number

    def __add__(self, other):
        new_number = self.faveolus_number +  other.faveolus_number
        new_cell = Cell(new_number)
        return new_cell

    def __sub__(self, other):
        sub_number = self.faveolus_number - other.faveolus_number

        if sub_number <= 0:
            raise OwnError("cannot sub")

        sub_cell = Cell(sub_number)
        return sub_cell

    def __mul__(self, other):
        multiple_number = self.faveolus_number * other.faveolus_number
        multiple_cell = Cell(multiple_number)
        return multiple_cell

    def __truediv__(self, other):
        division_number = round(self.faveolus_number / other.faveolus_number, 0)
        division_cell = Cell(division_number)
        return division_cell

    def make_order(self, faveolus_row, faveolus_number):
        one_faveolus = '*'
        return ((one_faveolus * faveolus_row + '\n') * (faveolus_number // faveolus_row) + one_faveolus * (faveolus_number % faveolus_row))

class OwnError(Exception):
    pass

cell = Cell(20)
cell_1 = Cell(1)
cell_2 = Cell(5)
new_cell = cell_1 + cell_2

cell_mul1 = Cell(2)
cell_mul2 = Cell(3)
multiple_cell = cell_mul1 * cell_mul2
cell_div1 = Cell(4)
cell_div2 = Cell(2)
division_cell = cell_div1 / cell_div2
print(f'Объединение клеток: {new_cell.faveolus_number}')

try:
    cell_sub1 = Cell(5)
    cell_sub2 = Cell(6)
    sub_cell = cell_sub1 - cell_sub2
    print(f'Вычетание клеток: {sub_cell.faveolus_number}')
except OwnError as err:
    print(err)

print(f'Создание общей клетки: {multiple_cell.faveolus_number}')
print(f'Создание общей клетки путем деления: {division_cell.faveolus_number}')
print(cell.make_order(5, 23))