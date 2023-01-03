# """
# Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len).

# Также в методе __new__ напишите условие для удаления пробелов и пустых строк в созданных словах.

# Создайте обьекты word1 и word2 класса Word и сделайте сравнения.
# """
# class Word:
#     def __new__(cls, string:str):
#         obj = super().__new__(cls)
#         obj.string = string.replace(" ", '')
#         return obj

#     # def __init__(self, string:str):
#     #     self.string = string.replace(' ', '')

#     def __len__(self):
#         return len(self.string)

#     def __eq__(self, other):
#         return len(self) == len(other)

#     def __gt__(self, other):
#         return len(self) > len(other)
    
#     def __lt__(self, other):
#         return len(self) < len(other)
    
#     def __ge__(self, other):
#         return len(self) >= len(other)
    
#     def __le__(self, other):
#         return len(self) <= len(other)

# word1 = Word("ab  c")
# word2 = Word("ABC")
# print(len(word1))
# print(word1 == word2)
# # word1.__eq__(word2)
# Word.__eq__(word1, word2)


class A:
    attr1 = 'hello'

    def __getattribute__(self, attr: str):
        print("__getattribute__", attr)
        return super().__getattribute__(attr)
    
    def __setattr__(self, attr: str, value):
        print("__setattr__")
        return super().__setattr__(attr, value)
    
    def __delattr__(self, attr: str):
        print("__delattr__")
        return super().__delattr__(attr)

    def __del__(self):
        print("__del__")
        del self

obj = A()
obj.attr1 # obj.__getattribute__('attr1')
obj.attr1 = 'world' # obj.__setattr__('attr1', 'world')
del obj.attr1 # obj.__delattr__('attr1')
del obj # obj.__del__()

getattr(obj, 'attr1') # obj.__getattribute__('attr1')
setattr(obj, 'attr1', 'world') # obj.__setattr__('attr1', 'world')
delattr(obj, 'attr1') # obj.__delattr__('attr1')
hasattr(obj, 'attr1') # True / False 'attr1' in dir(obj)
