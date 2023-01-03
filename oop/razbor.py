# декораторыX10    +
# try-except       -
# comprehensions   +
# build-ins
# files            +
# incapsulation
# тернарные выр-я

"Декораторы"
def decor(func):
    def wrapper(*args, **kwargs):
        print("функция начала работу")
        res = func(*args, **kwargs)
        print("функция закончила работу")
        return res
    return wrapper

# 1 вариант декорирования
@decor
def hello(string):
    print(string)
    return 10

hello("Hello world")

# 2 вариант декорирования
def hello(string):
    print(string)
    return 10

wrapper = decor(hello)
print(wrapper("Hello world"))


def call_function(func):
    def wrapper(*args, **kwargs):
        print(f'Вызываю функцию {func.__name__}')
        res = func(*args, **kwargs)
        print(f'Вызов функции {func.__name__} прошел успешно')
        return res
    return wrapper

@call_function
def hello():
    print("Hello world")

hello()


def make_bold(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<b>{res}</b>'
    return wrapper

def make_italic(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<i>{res}</i>'
    return wrapper

def make_underline(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return f'<u>{res}</u>'
    return wrapper

@make_bold
@make_italic
@make_underline
def hello():
    return 'Hello world'

print(hello())


def benchmark(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        start = datetime.now()
        res = func(*args, **kwargs)
        finish = datetime.now()
        time = finish - start
        print(f'Время выполнения: {time.total_seconds()} секунд.')
        return res
    return wrapper

@benchmark
def hello():
    import time
    time.sleep(5)

hello()


"comprehensions"
list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
new_list = [i for i in list_ if i > 0 and i % 2 == 0]
print(new_list) # [2, 4]

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
new_list = [int(i) for i in str_list]
print(new_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# "res1" if True else "res2"
new_list = [1 if i < 0 else i for i in list_]
print(new_list) # [1, 1, 1, 1, 0, 1, 2, 3, 4]

dict_ = {
    'Timur': {'history': 90, 'math': 95, 'literature': 91},
    'Olga': {'history': 92, 'math': 96, 'literature': 81},
    'Nik': {'history': 84, 'math': 85, 'literature': 87}
    }

new_dict = {
    key: title for key, value in dict_.items() 
    for title, grade in value.items() if grade == max(value.values())
    }
print(new_dict) # {'Timur': 'math', 'Olga': 'math', 'Nik': 'literature'}


list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude'] 

new_list = [len(name) for name in list_name]
print(new_list) # [4, 4, 6, 5, 4, 5, 4, 7, 5, 4]


# Создайте список list_ от 0 до 10 включительно c помощью специальной функции которая генерирует последовательно чисел,
# отфильтруйте список оставив в нем только четные элементы,
# затем разделите каждый элемент на 2 и выведите результат,
list_ = [i/2 for i in range(11) if i % 2 == 0]
list_ = [i/2 for i in range(0, 11, 2)]


set1 = {i for i in range(1, 11)}
set2 = {i for i in range(5, 15)}
full_set = set1.union(set2)

if len(full_set) == 20:
    print("Ваш объединенный сет полностью уникальный!")
else:
    intersections = 20 - len(full_set)
    print(f"В этом сете было {intersections} повторения, его длина составляет {len(full_set)}")


"files"
# open - функция принимающая название файла, вторым аргументор - режим (по дефолту чтение)

# f = open("test.txt")
with open("test.txt") as file:
    text = file.read() # считывает файл полностью
    file.seek(0) # перемещает каретку в начало, чтобы можно было считать еще раз
    text2 = file.read(5) # можно передать кол-во символов
    text3 = file.read()

# "r+" - чтение и запись (данные остаются, но можно записывать)
# "w+" - запись и чтение (данные удаляются, но можно читать и писать)
with open("test.txt", "r+") as file:
    # print(file.readable())  True
    # print(file.writable())  True
    file.seek(5)
    file.write("hello")



def reverse_file_print(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line[::-1])

# reverse_file_print("test.txt")

with open("task3.txt", "w+") as file: 
    # string = "*".join(map(str, range(10)))
    for i in range(10):
        file.write(f"{i}*")
    file.seek(0)
    print(file.read())

def calc_price(filename: str):
    res_sum = 0
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            data = line.split()
            res_sum += float(data[-1]) * float(data[-2])
    return res_sum

calc_price("prices.txt")
