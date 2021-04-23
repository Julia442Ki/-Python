# Задача_1

import time
class TrafficLight:
    _color = None
    _colors = ['красный', 'жёлтый', 'зелёный']

    def __init__(self):
        self._color = self._colors[0]

    def running(self):
        i=0
        while i<5:
            for el in TrafficLight._colors :
                print(el)
                i+=1
                time.sleep(1)

traffic = TrafficLight()
traffic.running()

print('___________')

# Задача_2

class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat road_to_village object')

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {intake} ton for the building')

road_to_village = Road(20000, 6)
road_to_village.intake()

print('___________')

# Задача_3

class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus

class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)
    def get_full_name(self):
        return self.name + self.surname
    def get_full_profit(self):
        self.__income = {'profit': self.profit, 'bonus': self.bonus}
        return self.__income

manager = Position('Petr', 'Petrov', 'manager', 500, 100)
print(manager.get_full_name(), manager.get_full_profit())

print('___________')