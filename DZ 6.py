# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав
# описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.

print("Задание 1 вар1")
from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = 'red', 'yellow', 'green'
    def running(self, red=7, yellow =2, green=1):
        #while True:
        print(self.__color[0], f' красный будет гореть в течении {red} секунд')
        sleep(red)
        print(self.__color[1], f' желтый будет гореть в течении {yellow} секунд')
        sleep(yellow)
        print(self.__color[2], f'Можно двигаться, у вас есть: {green} секунд')
        sleep(green)
        #print('Если надоест, то нажмите ctrl+c')
tLight = TrafficLight()
tLight.running(green=(int(input('введите сколько секунд будет гореть зеленый: '))))

print("Задание 1 вар2")
from time import sleep
from itertools import cycle
class TrafficLight:
    def __init__(self):
        self.__color = 'red', 'yellow', 'green'
    def running(self, red=7, yellow = 2, green=1):
        tColor = cycle(self.__color)
        #while True:
        print(next(tColor))
        sleep(next(cycle((red,yellow,green))))
tLight = TrafficLight()
tLight.running(green=3)


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
#
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для
# покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
print("Задание 2")
class Road:
    def __init__(self):
        self._length = 20
        self._width = 5000

    def calc(self, mass=1,depth=1):
        return self._length * self._width * mass * depth
calcRoad= Road()
print('получаетя масса: {} тонн'.format(int(calcRoad.calc(mass=25, depth=5)/1000)))

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

print("Задание 3")
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income1 = income['wage']
        self.income2 = income['bonus']
class Position(Worker):
    def get_full_name(self):
        return 'сотрудника зовут: {} {}'.format(self.name,self.surname)
    def get_total_income(self):
        return 'позиция сотруднкиа: {}\nс доходом: {} rub в месяц'.format(self.position, self.income1+self.income2)

print(Position('Andrey', 'Podin', 'sales', {"wage": 200000, "bonus": 90000}).get_full_name())
print(Position('Andrey', 'Podin', 'sales', {"wage": 200000, "bonus": 90000}).get_total_income())

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
# автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
print("Задание 4")
class Car:
    def __init__(self, speed=30, color='black', name='audi', is_police= False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f'машина {self.name} едет ')
    def stop(self):
        print('машина остановилась')
    def turn(self, direction):
        print(f'Машина повернула {direction}')
    def show_speed(self):
        print(f'Вы едите на {self.name} цвет {self.color} и Ваша скорость равна {self.speed}')
class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'You speed is more than {self.speed}. Hey man, slow down')
class SportCar(Car):
        pass
class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed> 40:
            print(f'You speed is more than {self.speed}. Move slowly, very slowly!')
        else:
            print('normal speed, good trip')

class PoliceCar(Car):
        pass

TownCar(100,'blue','wv', True).show_speed()
SportCar(color='red', speed=200, is_police= True, name='porshe').show_speed()
WorkCar().show_speed()
PoliceCar(50, 'green','uaz', True).show_speed()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов методы
# должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

print("Задание 5")
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('А теперь могучая ручка!! Ураааа!')

class Pencil(Stationery):
    def draw(self):
        print('Невероятный карандаш!')

class Handle(Stationery):
    def draw(self):
        print('Супер маркер!!!!!')

Pen.draw('')
Pencil.draw('')
Handle.draw('')



