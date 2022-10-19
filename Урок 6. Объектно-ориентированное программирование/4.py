# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} машина заведена'

    def stop(self):
        return f'{self.name} машина остановлена'

    def turn_direction(self, direction):
        return f'{self.name} направилась {direction}'

    def show_speed(self):
        return f'текущая скорость автомобиля {self.name} составляет {self.speed}'




class Towncar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'скорость {self.name}больше 40 км.ч'
        else:
            return f'Скорость {self.name} меньше 40 кмч'


class Sportcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class Workcar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f' Текущая скорость {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'скорость {self.name} больше 60 км.ч'
        else:
            return f'Скорость {self.name} меньше 60 кмч'

class Policecar(Car):
    def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police:
            return f'{self.name} это полицейский автомобиль'
        else:
            return f'{self.name} это не полицейский автомобиль'


audi = Sportcar ('100', 'black', 'audi', False)
bmw = Towncar ('80', 'white', 'bmw', False )
mercedes = Workcar (60, 'Red', 'mercedes', False)
ford = Policecar ('160', 'black and white', 'ford', True)

print(audi.turn_direction('В москву'))
print(audi.go())
print(f'{audi.name}, со скоростью {audi.speed}')
print( f'{audi.name} полицейский автомобиль? {audi.is_police}')
print(ford.police())
print(audi.show_speed())