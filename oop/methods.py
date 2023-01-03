"существует 3 вида методов"
# instance methods - обычнфе методы, которые принимают первым аргументом self (ссылка на обьект). нужны они для работы с аттрибутами обьекта. 

class A:
    def instance_method(self):
        print("метод обьекта")
        print("первый аргумент:", self)

obj_a = A()
obj_a.instance_method() # если вызываем у обьекта, то self передается автоматически
A.instance_method(obj_a) # если вызываем у класса, то в self нужно передать обьект от этого класса



# class methods - методы, которые принимают первым аргументом cls (ссылка на класс). нужны они для создания обьектов или изменения аттрибутов класса. для создания метода класса нужно задекорировать его classmethod

class B:
    @classmethod
    def class_method(cls):
        print("класс метод")
        print("первый аргумент:", cls)

obj_b = B()
B.class_method() # class B
obj_b.class_method() # class B
# не важно будем ли вызывать класс метод у класса или у обьекта, в первый аргумент придет ссылка на класс

class C:
    counter = 0

    def __init__(self):
        self._inc_counter()

    def __del__(self):
        self._dec_counter()
        del self

    @classmethod
    def _inc_counter(cls):
        cls.counter += 1

    @classmethod
    def _dec_counter(cls):
        cls.counter -= 1

obj1 = C()
obj2 = C()
obj3 = C()
del obj2
print(C.counter)


class Pizza:
    def __init__(self, radius, *ingredients):
        self.r = radius
        self.ingredients = ingredients
    
    def cook(self):
        print(f"готовится пицца размером {self.r*2} см")
        print(f"Ингридиенты: {self.ingredients}")

    @classmethod
    def four_cheeze(cls, r):
        pizza = cls(r, "Моцарелла", "Дор блю", "Чеддер", "Голландский")
        return pizza

pizza1 = Pizza(15, "пеперони", "Моцарелла", "Ананас")
# pizza2 = Pizza(15, "Моцарелла", "Дор блю", "Чеддер", "Голландский")
# pizza3 = Pizza(20, "Моцарелла", "Дор блю", "Чеддер", "Голландский")
pizza2 = Pizza.four_cheeze(15)
pizza3 = Pizza.four_cheeze(20)

pizzas = [pizza1, pizza2, pizza3]
for i in pizzas:
    i.cook()



# static methods - просто функции внутри класса, которые не взаимодействуют ни с классом, ни с обьектом. находятся они внутри класса лишь потому, что они используются только внутри класса и вне они в целом бесполезны. чтобы создать static метод, нужно его задекорировать staticmethod

class D:
    @staticmethod
    def hello(string):
        print(string)

obj_d = D()
obj_d.hello("Hello world")
D.hello("Hello world")


class Cylinder:
    def __init__(self, diameter, hight):
        self.di = diameter
        self.h = hight
        self.area = self.get_area(diameter, hight)

    @staticmethod
    def get_area(di, h):
        from math import pi
        circle = pi * di**2 / 4
        side = pi * di * h
        area = circle * 2 + side
        return round(area, 2)

cylinder1 = Cylinder(4, 10)
print(cylinder1.area)

area2 = Cylinder.get_area(2, 5)
print(area2)



# def get_area_cylinder(di, h):
#     from math import pi
#     circle = pi * di**2 / 4
#     side = pi * di * h
#     area = circle * 2 + side
#     return round(area, 2)

# class Cylinder:
#     def __init__(self, diameter, hight):
#         self.di = diameter
#         self.h = hight
#         self.area = get_area_cylinder(diameter, hight)
