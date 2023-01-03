"Магические методы (dunder - double underscore) - методы, у которых 2 нижних подчеркивания в начале и 2 в конце. магия в том, что мы их не вызываем напрямую, а они вызываются определенными операторами или функциями"

# __new__, __init__ - вызываются, когда создаем обьект 
int(5)

# __add__
'5' + '5'
'5'.__add__('5')

# __str__
a = 5

str(a)
f"a = {a}"
a.__str__()

print(a)
a.__str__()

# __hash__
hash('aaa')
'aaa'.__hash__()


# __eq__
a = 6
b = 7

a == b
a.__eq__(b)

# __ne__
a != b
a.__ne__(b)

# __lt__ <
a < b
a.__lt__(b)

# __gt__ >
# __le__ <=
# __ge__ >=


# __getattribute__
string = 'hello'
string.lower
string.__getattribute__('lower')

getattr(string, 'fdskhklrsuf', None)
string.__getattribute__('fdskhklrsuf')
# getattr - функция, которая вызывает __getattribute__. если такого нет и был передан default, то ошибка не вызовется
# __getattribute__ - метод, который вызывает ошибку если такого аттрибута нет


# __setattr__
a = 'hello'

a.new_attr = 'NEW ATTRIBUTE'
a.__setattr__('new_attr', 'NEW ATTRIBUTE')

setattr(a, 'new_attr', 'NEW ATTRIBUTE')
a.__setattr__('new_attr', 'NEW ATTRIBUTE')


# __getitem__ - когда мы обращаемся в квадратных скобочках (по индексу, по ключу, делаем срезы)
string = 'hello'
string[0]
string.__getitem__(0)

dict_ = {"a":1, "b":2}
dict_['a']
dict_.__getitem__('a')


# __iter__ - вызывается, когда мы итерируем обьект
class A:
    def __iter__(self):
        for i in range(10):
            print("iter method")
            yield i

for i in A():
    print(i)

def generator():
    for i in range(10):
        yield i

gen = generator()

while True:
    try:
        print(next(gen))
    except StopIteration:
        break
