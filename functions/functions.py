"===============================Функции==============================="
# функция - именнованный блок кода, который может принимать аргументы и возвращать результат

def my_sum(x, y):
    return x+y

res = my_sum(5,6)
print("res",res)

def my_len(obj):
    count = 0
    for element in obj:
        count += 1
        # count = count + 1
    return count

res = my_len(['abc',1,2,3])
print(res)

list_ = ['abc',1,2,3]
count = 0
for element in list_:
    count += 1
print(count)

str_ = 'abcde'
count = 0
for element in str_:
    count += 1
print(count)

"Функции соблюдают принцип DRY (don't repeat yourself)"

"================================Аргументы и параметры================================"
# параметры - переменные внутри функции, значения которым мы задаем при вызове функции (те переменные, которые мы пишем в круглых скобочках, когда пишем def)
# аргументы - значения, которые мы передаем при вызове функции

"===================================Виды параметров==================================="
# 1. обязательные
# 2. не обязательные
# 2.1 с дефолтом (со значением по умолчанию)
# 2.2 args (все позиционные аргументы, которые не попали в обязательные и с дефолтом)
# 2.3 kwargs (все лишние именнованные аргументы)

"===================================Виды аргументов==================================="
# 1. позиционные (по позиции)
# 2. именнованные (по названию (параметр=значение))

def add_or_add_10(num1:int, num2=10) -> int:
    """
    Складывает 2 числа

    Если второе число не передать, сложит первое с 10
    """
    return num1 + num2

number1 = 5
print(add_or_add_10(number1, 6))  # 11
print(add_or_add_10(5))  # 15


"-------------*-------------"
list1 = list(range(1, 11))
list2 = [*range(1,11)]
print(list2)  # [1,2,3,4,5,6,7,8,9,10]

dict1 = {"a":1, "b":2, "c":3}
dict2 = {**dict1}  # {"a":1, "b":2, "c":3}
list3 = [*dict1]  # ['a', 'b', 'c']
print(dict2)
print(list3)


def func(a, b=10, *args, **kwargs):
    print('a -', a)
    print('b -', b)
    print('args -', args)
    print('kwargs -', kwargs)

# func() - TypeError: func() missing 1 required positional argument: 'a'

func(20) 
# a - 20
# b - 10
# args - ()
# kwargs - {}

func(20, 30)
# a - 20
# b - 30
# args - ()
# kwargs - {}

func(b=30, a=10)
# a - 10
# b - 30
# args - ()
# kwargs - {}

func(40,50,60,70,80)
# a - 40
# b - 50
# args - (60, 70, 80)
# kwargs - {}

func(10, 15, 20, hello='hello world')
# a - 10
# b - 15
# args - (20,)
# kwargs - {'hello': 'hello world'}

func(10, c=5, d=[1,2,3], e=True, f=None)
# a - 10
# b - 10
# args - ()
# kwargs - {'c': 5, 'd': [1, 2, 3], 'e': True, 'f': None}


"=======================================Lambda======================================="
# lambda - анонимная функция, которая записывается в одну строку
lamda_func = lambda x: x**10
print(lamda_func(5))  # 9765625 = 5 ** 10

"====================================Калькулятор===================================="
calc = {
    '+': lambda n1, n2: n1 + n2,
    '-': lambda n1, n2: n1 - n2,
    '*': lambda n1, n2: n1 * n2,
    '**': lambda n1, n2: n1 ** n2,
    '/': lambda n1, n2: n1 / n2,
    '//': lambda n1, n2: n1 // n2,
    '%': lambda n1, n2: n1 % n2,
}

def main():
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        oper = input("Введите операцию: ")
        func = calc[oper]
        res = func(num1, num2)

        print(num1, oper, num2, '=', res) 

    except ValueError:
        print('Введите число')
    except KeyError:
        print('Операция не верная')
    except ZeroDivisionError:
        print('На 0 делить нельзя')

# while True:
#     main()
#     if input('завершить (y/n)? ').lower() == 'y':
#         break


db = [
    {'name':'Hello', 'password':hash('12345678')},
    {'name':'World', 'password':hash('hello world')},
]

def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password1, password2):
    if in_database(name):
        raise Exception('Юзер с таким именем уже существует')
    if password1 != password2:
        raise Exception('Пароли не совпадают')
    user = {'name':name, 'password':hash(password1)}
    db.append(user)
    return 'Вы успешно зарегистрировались'

def login(name, password):
    if not in_database(name):
        raise Exception('Пользователь не найден!')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный!')
    return 'Вы успешно залогинились'

def main():
    print("Добро пожаловать")
    while True:
        try:
            action = input('Register:1, Login:2, Quit:3\n')

            if action == '3':
                break
            elif action == '1':
                name = input('Введите имя: ')
                p1 = input('Введите пароль: ')
                p2 = input('Повторите пароль: ')
                print(register(name, p1, p2))
            elif action == '2':
                name = input('Введите имя: ')
                password = input('Введите пароль: ')
                print(login(name, password))
            else:
                print('Не корректный выбор')
        except Exception as error:
            print(error)

# main()


def translate(string:str) -> str:
    eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    ru = "йцукенгшщзхъфывапролджэячсмитьбю"
    if string[0] in eng:
        dictionary = str.maketrans(eng, ru)
    else:
        dictionary = str.maketrans(ru, eng)
    return string.translate(dictionary)

print(translate('руддщ'))  # hello
print(translate('ghbdtn'))  # привет


# list_ = [1,2,3,4,5]
# print(list_[0])
# print(list_[1])
# print(list_[2])
# print(list_[3])
# print(list_[4])

# for i in list_:
#     print(i)


# list_ = [1,2,3,4,5,6]
# len_ = 0
# for el in list_:
#     len_ += 1

# string = '123456780'
# len_ = 0
# for el in string:
#     len_ += 1

# tuple = (1,3,5)
# len_ = 0
# for el in tuple:
#     len_ += 1

def my_len(obj):
    len_ = 0
    for el in obj:
        len_ += 1
    return len_

list_ = [1,2,3,4,5,6]
my_len(list_)

string = '123456780'
my_len(string)
