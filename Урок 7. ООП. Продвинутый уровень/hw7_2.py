 # 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
# этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return self.width / 6.5 + 0.5

    def get_square_jacket(self):
        return self.height * 2 + 0.3

    @property
    def get_sq(self):
        return str(f'Общая площадь \n'
                   f' {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.square_coat}'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_jacket = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.square_jacket}'

coat = Coat(0.5, 1)
jacket = Jacket(1.5, 0.7)
print(coat)
print(jacket)
print(coat.get_sq)
print(jacket.get_sq)
print(jacket.get_square_coat())
print(jacket.get_square_jacket())