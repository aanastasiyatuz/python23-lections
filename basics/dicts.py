"==============================Словари=============================="
# dict - изменяемый, итерируемый, неупорядоченный, неиндексируемый тип данных, для хранения данных в парах (ключ:значение)

user = {
    "name": "Nastya",
    "age":13,
    "last_name":"Tuz"
}

print(user["name"])  # "Nastya"

# ключами в словаре могут быть только не изменяемые типы данных

dict1 = {"a":1, "b":2, "a":3, "a":4}
print(dict1["a"])  # 4 (если ключи одинаковые, сохранится только последнее значение)

# print(dict1["c"])  # KeyError: 'c'


"================================Создание================================"
dict1 = {"a":1, "b":2}
dict2 = dict( [ ("a", 1), ("b", 2) ] )
# {"a":1, "b":2}

dict3 = dict( ["ab", "cd", "ef"] )
# {"a":"b", "c":"d", "e":"f"}

dict4 = {}
dict4["name"] = "Nastya"
dict4["age"] = 13
# {"name":"Nastya", "age":13}


"=================================Методы словаря================================="
# get - метод, который возвращает значение по ключу, если такого ключа нет, то возвращает None или дефолтное значение
user = {
    "name": "Nastya",
    "age":13,
    "last_name":"Tuz"
}

# user["id"]  # KeyError
user.get("id")  # None
user.get("name")  # "Nastya"
user.get("id", 1)  # 1
user.get("name", "User")  # "Nastya"


# pop - удаляет пару по ключу и возвращает значение
dict1 = {"a":1, "b":2, "c":3}
popped = dict1.pop("a")
# dict1 = {"b":2, "c":3}
# popped = 1

# dict1.pop("d")  # KeyError: 'd'
# del dict1["d"]  # KeyError: 'd'


# popitem - удаляет последнюю пару и возвращает ее
dict1 = {"a":1, "b":2, "c":3}
popped = dict1.popitem()
# dict1 = {"a":1, "b":2}
# popped = ("c", 3)


# update - расширяет словарь парами из второго словаря
dict1 = {1:"a", 2:"b"}
dict2 = {2:"c", 3:"d"}

dict1.update(dict2)
print(dict1)
# {1:"a", 2:"c", 3:"d"}
print(dict2)
# {2:"c", 3:"d"}


# clear - очищает словарь
dict1.clear()
print(dict1) # {}


# fromkeys - метод для создания нового словаря, используя список ключей
dict1 = dict.fromkeys("hi")
print(dict1)
# {"h":None, "i":None}

dict2 = dict.fromkeys([1,2,3])
print(dict2)
# {1:None, 2:None, 3:None}

dict3 = dict.fromkeys([1,2,3], "Hello")
print(dict3)
# {1:"Hello", 2:"Hello", 3:"Hello"}


# keys, values, items
# keys - метод, который возвращает ключи
# values - метод, который возвращает значения
# items - метод, который возвращает пары ключ - значение в виде tuple
user = {
    "name": "Nastya",
    "age":13,
    "last_name":"Tuz"
}
print(user.keys())  # dict_keys(['name', 'age', 'last_name'])
print(user.values())  # dict_values(['Nastya', 13, 'Tuz'])
print(user.items())  # dict_items([('name', 'Nastya'), ('age', 13), ('last_name', 'Tuz')])


"==============================Итерирование словарей=============================="
user = {
    "name": "Nastya",
    "age":13,
    "last_name":"Tuz"
}

for key in user:
    print(key)
    # при итерации словаря будут приходить ключи

for key in user.keys():
    print(key)
    # при итерации dict_keys тоже приходят ключи

for value in user.values():
    print(value)
    # при итерации dict_values приходят значения

for items in user.items():
    print(items)
    # items[0] - ключ
    # items[1] - значение
    # при итерации dict_items приходят пары в tuple

items = ('name', 'Nastya')
key, value = ('name', 'Nastya')

for key, value in user.items():
    print(key, value)


# вам дан словарь
dict1 = {"a":1, "b":2, "c":3}
# создайте новый словарь, поменяв ключи со значениями
# {1:"a", 2:"b", 3:"c"}

dict2 = {}
for key, value in dict1.items():
    dict2[value] = key
print(dict2)
# {1:"a", 2:"b", 3:"c"}
