"========================================OOP========================================"
# OOP - Object-orientated programing
# ООП - Обьектно ориентированное программирование (парадигма) 

class Person:
    # переменные внутри класса (обьекта) - аттрибуты
    arms = 2
    legs = 2

    # функции внутри класса (обьекта) - методы
    def __init__(self, name, age):
        # __init__ - метод, который будет добавлять в обьект те аттрибуты в обьект, которые отличаются у разных обьектов
        # self - ссылка на обьект, который только что создался
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} ходит')

    def happy_birthday(self):
        print(f"{self.name}, Happy birthday!")
        self.age += 1
        return "Подарок"

# obj1 = Person()
# obj2 = Person()
obj1 = Person('Nastya', 12)
obj2 = Person('Anonym', 23)
print(obj1.name) # Nastya
print(obj2.name) # Anonym
obj1.walk()
obj2.walk()
obj1.arms # 2
obj2.arms # 2
# Person.name # AttributeError: type object 'Person' has no attribute 'name'
obj1.hello = 'Hello'
print(obj1.hello) # Hello
# print(obj2.hello) # AttributeError: 'Person' object has no attribute 'hello'
print("AGE:", obj1.age)
obj1.happy_birthday()
obj1.happy_birthday()
obj1.happy_birthday()
print("AGE:", obj1.age)



"===================================Обьекты класса==================================="
# обьект, экземпляр, instance класса - обьект, созданный по шаблону класса (он перенимает все аттрибуты и методы класса)

"=================================Аттрибуты и методы================================="
# аттрибуты - переменные
# методы - функции

class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная обьекта'

    def __str__(self):
        return 'обьект от класса А'

print(dir(A))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']
# нет var2

obj = A()
print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

print(obj) # обьект от класса А


"Класс не имеет доступа к обьектам"

"С помощью аттрибута __class__ мы можем обратиться к классу от которого создан обьект"
print(obj.__class__) # <class '__main__.A'>
print(A.__class__) # <class 'type'>
print(type.__class__) # <class 'type'>
"Обьекты-классы создаются от мета-класса type"


class Calc:
    def add(self, a, b):
        "Функция сложения"
        return a + b

    def sqrt(self, num, ndigits=2):
        "Функция нахождения квадратного корня числа с округлением"
        import math
        sqrt_num = math.sqrt(num)
        return round(sqrt_num, ndigits)

    def percent(self, total, _percent):
        "Функция нахождения процента от числа"
        return (total * _percent) / 100

    def super_func(self, string):
        "Функция, которая выполняет вычисления в строке"
        return eval(string)

calc = Calc()
print(calc.add(4,5)) # 9
print(calc.sqrt(2, 10)) # 1.4142135624
print(calc.sqrt(2)) # 1.41
print(calc.percent(60, 10)) # 6.0
print(calc.percent(258, 20)) # 51.6
print(calc.super_func('(5-7)**2 - 10')) # -6


class B:
    var = 4

    def __init__(self, a):
        self.a = a

obj = object.__new__(B)
# obj.var  # 4
# obj.a # AttributeError
B.__init__(obj, 5)
# obj.__init__(5)
# obj.var # 4
# obj.a # 5

obj = B(5)


class Sniper:
    health = 100

    def __init__(self, name):
        self.name = name

    def shoot(self, sniper2):
        sniper2.health -= 20
        print(f'атаковал {self}')
        print(f'у {sniper2} осталось {sniper2.health}')

    def __str__(self):
        # когда принтим обьект
        # когда оборачиваем в строку
        return self.name

sniper1 = Sniper('1')
sniper2 = Sniper('2')

import random
while sniper1.health and sniper2.health:
    choice = random.randint(1,2)
    if choice == 1:
        sniper1.shoot(sniper2)
    else:
        sniper2.shoot(sniper1)

if sniper1.health:
    print(f'Победил {sniper1}')
else:
    print(f'Победил {sniper2}')
