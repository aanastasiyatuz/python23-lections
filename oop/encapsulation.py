"Инкапсуляция - принцип ООП, у которого есть 2 трактовки"
# 1. сбор всех необходимых аттрибутов в одну "капсулу" (класс)
# 2. сокрытие данных (ограничение доступа к аттрибутам)

"Виды доступа к аттрибутам"
# 1. public (публичные)
# 2. protected (защищенные) - с одним underscore в начале
# 3. private (приватные) - с двумя underscore в начале

class A:
    attr1 = 'public'
    _attr2 = 'protected'
    __attr3 = 'private'

print(A.attr1) # public
print(A._attr2) # protected
# print(A.__attr3) # AttributeError: type object 'A' has no attribute '__attr3'
print(A._A__attr3) # protected

"obj.__dict__ - словарь с переменными обьекта"
# print(A.__dict__)

class B:
    x = 'hello'

    def __init__(self):
        self.y = 'world'

obj_b = B()
print(obj_b.__dict__) # {'y':'world'}

obj_b.hello = 'HELLO'
print(obj_b.__dict__) # {'y': 'world', 'hello': 'HELLO'}

setattr(obj_b, 'new', 'NEW VAL')
print(obj_b.__dict__) # {'y': 'world', 'hello': 'HELLO', 'new': 'NEW VAL'}


"------------------------Getters/Setters------------------------"
# функции, с помощью которых можно получать/изменять значение аттрибута

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception('Возраст не может быть меньше 0 или больше 120')

obj = Person('Nastya', 12)
print(obj.get_age()) # 12
obj.set_age(50)
print(obj.get_age()) # 50
# obj.set_age(234) # Exception


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    "декоратор property делает из функции аттрибут"
    @property 
    def age(self):
        return self.__age

    @age.getter # переопределяет __getattribute__ в обьекте age (property)
    def age(self):
        return self.__age

    "декоратор setter вызывается когда пишется obj.age = value"
    @age.setter # переопределяет __setattr__ в обьекте age (property)
    def age(self, new_age):
        if type(new_age) != int:
            raise Exception('Возраст должен быть числом')
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else:
            raise Exception('Возраст не может быть меньше 0 или больше 120')

    "декоратор deleter вызывается когда пишется del obj.age"
    @age.deleter # переопределяет __delattr__ в обьекте age (property)
    def age(self):
        if self.__age < 100:
            raise Exception('Нельзя удалять возраст')
        del self.__age

obj = Person('Nastya', 12)
print(obj.age)
obj.age = 115    # obj.age(115) # @age.setter
# obj.age = -243   # Exception
del obj.age   # obj.age() # @age.deleter
print(obj.__dict__)


class Phone:
    def __init__(self, number):
        "+996 777 01-01-01"
        self.__number = number
    
    @property
    def number(self):
        """функция для получения значения"""
        return self.__number
    
    @number.setter
    def number(self, new_number):
        """функция для изменения значения"""
        assert type(new_number) == str, 'Номер должен быть строкой'
        assert len(new_number) == 9, 'Номер должен состоять из 9 цифр'
        n = new_number
        self.__number = f"+996 {n[:3]} {n[3:5]}-{n[5:7]}-{n[7:]}"

obj = Phone("+996 777 01-01-01")
print(obj.number)
obj.number = '123456789'
print(obj.number) 

# obj = Person('dsg', 32)
# age = property(obj.age)
# obj.age = age