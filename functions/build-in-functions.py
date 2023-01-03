"=========================Встроенные функции========================="
# map, filter, reduce, zip, enumerate

# zip - соединяет несколько последовательностей (получаем генератор, в котором элементы - tuple)

list1 = [1,2,3,4,5]
list2 = ['a', 'b', 'c']
list3 = [10.5, 20.6, 30.8, 40.7]

zipped = zip(list1, list2, list3) # <zip object at 0x7f8abbf57cc0>
for el in zipped:
    print(el)
# (1, 'a', 10.5)
# (2, 'b', 20.6)
# (3, 'c', 30.8)

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
dict_ = dict(zip(list1, list2)) # {1:'a', 2:'b', 3:'c', 4:'d', 5:'e'}

# enumerate - нумерует последовательность (по дефолту с 0) (тоже получаем генератор)
enumerated = enumerate('hello') # <enumerate object at 0x7f8e6557ee00>
for el in enumerated:
    print(el)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

string = 'hello world'
print(list(enumerate(string[5:]))) 
# [(0,' '), (1,'w'), (2,'o'), (3,'r'), (4,'l'), (5,'d')]

print(list(enumerate(string, 100))) 
# [(100,'h'),(101,'e'),(102,'l'),(103,'l'),(104,'o'),(105,''),(106,'w'),(107,'o'),(108,'r'),(109,'l'),(110,'d')]



# map - принимает функцию и последовательность (записывает в новую последовательность результат функции, в которую передаются элементы последовательности)

list_ = ['1', '2', '3', '4']
mapped = map(int, list_) # <map object at 0x7fd06b532e50>
print(list(mapped)) # [1, 2, 3, 4]

string = 'hello world'
res = ''.join(map(lambda x:x.upper(), string))
print(res) # 'HELLO WORLD'

list_ = [1,2,3,4,5]
print(list(map(lambda x: x**2, list_)))
# [1, 4, 9, 16, 25]

list_ = [1,2,3,4,5]
def to_2_degree(x):
    return x ** 2
print(list(map(to_2_degree, list_)))
# [1, 4, 9, 16, 25]

# new_list = []
# for el in list_:
#     new_list.append(to_2_degree(el))


# filter - возвращает генератор, с элементами, прошедшими фильтр (какое-то условие), принимает функцию и последовательность

list_ = [3, -5, 0, 10, -34]
filtered = filter(lambda x: x > 0, list_) # <filter object at 0x7f1191c0d370>
print(list(filtered)) # [3, 10]

users = [
    {'name':'Nastya', 'age':10},
    {'name':'Makers', 'age':4},
    {'name':'Anonym', 'age':25}
]
# оставить пользователей, которые старше 12
res = list(filter(lambda user: user['age']>12, users))
print(res) # [{'name': 'Anonym', 'age': 25}]

# вывести только имена пользователей, которые старше 9
filtered = filter(lambda x:x['age']>9, users)
res = list(map(lambda x:x['name'], filtered))
print(res) # ['Nastya', 'Anonym']


# reduce - принимает функцию и последовательность, возвращает 1 результат (передаваемая функция должна принимать 2 аргумента)
from functools import reduce

list_ = [1,4,3,6,10,5]
res = reduce(lambda x,y: x*y, list_)
print(res) # 3600 = 1*4*3*6*10*5

string = 'hello'
res = reduce(lambda x, y: x+"$"+y, string)
print(res) # 'h$e$l$l$o'
# x = 'h', y = 'e' -> 'h$e'
# x = 'h$e', y = 'l' -> 'h$e$l'
# x = 'h$e$l', y = 'l' -> 'h$e$l$l'
# x = 'h$e$l$l', y = 'o' -> 'h$e$l$l$o'

string = 'hello world'
print(reduce(lambda x,y: x.replace(y, '!'), string)) # 'h'
# x = 'h', y = 'e' -> 'h'.replace('e', '!') -> 'h'
# x = 'h', y = 'l' -> 'h'.replace('l', '!') -> 'h'
# x = 'h', y = 'l' -> 'h'.replace('l', '!') -> 'h'
# x = 'h', y = 'o' -> 'h'.replace('o', '!') -> 'h'


print(reduce(lambda x,y:string.replace(x,y), string))
# x = 'h', y = 'e' -> 'eello world'
# x = 'eello world', y = 'l' -> 'hello world'.replace(x, y) -> 'hello world'
# x = 'hello world', y = 'l' -> 'hello world'.replace(x,y) -> 'l'




list_ = [1,2,4,6,1,9,-1,6,-12]
# выведите самое маленькое число, с помощью reduce

res = reduce(lambda x,y:x if x<y else y, list_)

users = [
    {'name':'Nastya', 'age':10},
    {'name':'Makers', 'age':4},
    {'name':'Anonym', 'age':25}
]
# выведите самого младшего пользователя, с помощью reduce
def min_dict(dict1, dict2):
    if dict1['age'] < dict2['age']:
        return dict1
    return dict2

res = reduce(min_dict, users)
print(res)

res = reduce(lambda x,y:x if x['age']<y['age'] else y, users)

# выведите только имя самого младшего пользователя
print(res['name'])
