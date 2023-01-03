"===============================JSON==============================="
# JavaScript Object Notation - универсальный формат, в котором мы можем храть данные в типах данных, понятных почти для всех языков программирования

import json

json_list = "[1,2,3,4,5]"
print(type(json_list)) # <class 'str'>

python_list = json.loads(json_list)
print(type(python_list)) # <class 'list'>

# десериализация - перевод с json строки в python обьекты
# loads - метод для десериализации с json строки
# load - метод для десериализации с json файла

# сериализация - перевод python обьектов в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериализации в json файл

with open('test.json') as file:
    list_ = json.load(file)

# list_.append((1,2,3)) # переконвертируется в list
# list_.append(True) # запишется как true
# list_.append(None) # запишется как null
# list_.append({"1","2","3"}) # TypeError: Object of type set is not JSON serializable
# list_.append('hello')  # "hello"
# list_.append({1:"hello", 2:"world"})  # {"1":"hello","2":"world"}

with open('test.json', 'w') as file:
    json.dump(list_, file)
