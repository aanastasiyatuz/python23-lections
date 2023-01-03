"==========================Области видимости=========================="
# LEGB - local enclosed global build-in

"==============================Build-in=============================="
# втроенное пространство имен (list, sum, dict, print, input)

"===============================Global==============================="
# все переменные, которые мы создали внутри одного файла
# чтобы посмотреть все глобальные переменные, можно использовать globals
a = 5
b = 'hello'
print(globals())

"==============================Enclosed=============================="
# замкнутое пространство имен - локальное пространство, у которого есть внутреннее локальное пространство

var = 'global'

def func():
    # локальное пространство для глобального пространства
    # замкнутое пространство (потому что есть более локальное пространство)
    var = 'enclosed'
    def inner_func():
        # локальное пространство для пространства func
        var = 'local'
        print(var)
    print(var)
    inner_func()

print(var)
func()
# global enclosed local


"===============================Local==============================="
# локальное пространство имен - переменные, созданные внутри функции

a = 10

def func(a, b):
    print("GLOBALS",globals())
    print("LOCALS",locals())
    print(a, b)

# func(5, 7)


count = 1

def increase_count():
    global count
    print(count)
    count += 1

increase_count() # 1
increase_count() # 2
increase_count() # 3
increase_count() # 4



def count(i):
    counter = 0

    def increase_counter():
        nonlocal counter
        # доступ на изменение переменной замкнутого пространства
        print(counter)
        counter += 1
    
    for _ in range(i):
        increase_counter()

count(10)
# 0 1 2 3 4 5 6 7 8 9


def func():
    local_var = 5

func()
# print(local_val)  NameError
func()