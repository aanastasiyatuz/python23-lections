"Наследование - принцип ООП, в котором мы можем унаследовать, переопределить и использовать в дочернем классе все аттрибуты и методы родительского класса"

class A:
    def method(self):
        print('Метод в классе A')

obj_a = A()
obj_a.method() # Метод в классе A

class B(A):
    """
    Наследовали все методы и аттрибуты у класса А
    """

obj_b = B()
obj_b.method() # Метод в классе A

class C(A):
    """
    Наследовали все методы и аттрибуты у класса А
    и переопределили метод method
    """

    def method(self):
        print('Метод в классе C')

obj_c = C()
obj_c.method() # Метод в классе C

obj_a = A()
obj_a.method() # Метод в классе A

class A:
    x = 'x in A'
    y = 'y in A'

class B(A):
    x = 'x in B'

print(A.x) # x in A
print(A.y) # y in A
print(B.x) # x in B
print(B.y) # y in A

"mro (method resolution order) - порядок поиска аттрибутов"
print(B.mro()) 
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(dir(object))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']


class A:
    def my_range(self, n):
        return list(range(n+1))

print(A().my_range(5))
# [0,1,2,3,4,5]

class B(A):
    def my_range(self):
        # return A.my_range(self, 10)
        "через super() мы обращаемся к родительскому классу"
        return super().my_range(10)

print(B().my_range())
# [0,1,2,3,4,5,6,7,8,9,10]


"----------------------Виды наследований----------------------"
# одиночное наследование (когда мы наследуемся в дочернем классе от 1 класса)
# множественное наследование (когда мы наследуемся в дочернем классе от нескольких классов)
# многоуровневое наследование (когда мы наследуемся от класса у которого есть родитель)
# иерархическое наследование (когда от одного родителя много дочерних классов)
# гибридное наследование (когда используются несколько видов наследования)

"=====================Множественное наследование====================="
class A:
    a = 'a'

class B:
    b = 'b'

class C(A,B):
    """Наследовали все аттрибуты у классов A и В"""
    c = 'c'

obj_c = C()
obj_c.a # a
obj_c.b # b
obj_c.c # c

class A:
    def method(self):
        print('Метод в классе А')

class B:
    def method(self):
        print('Метод в классе B')

class C(A,B):
    ...

obj_c = C()
obj_c.method() # Метод в классе A
print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

"---------------Проблемы множественного наследования---------------"
# Проблема ромба (решенная с помощью mro) 

class A: 
    ...
    # def __str__(self):
    #     return "A"

class B:
    ...
    # def __str__(self):
    #     return "B"

class C(A,B): 
    ...
    # def __str__(self):
    #     return "C"

obj_c = C()
print(obj_c)


# проблема перекрестного наследования (не решенная)
class A:
    ...

class B:
    ...

class D(A,B):
    ...

class E(B,A):
    ...

# class F(D,E):
#     ...

