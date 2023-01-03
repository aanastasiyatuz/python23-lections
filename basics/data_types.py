"======================Переменные======================"
# переменные - это ссылки на ячейки памяти, где хранятся какие-то данные, для дальнейшего использования этих данных, при обращении к названию переменной

num1 = 10
num2 = 45
print(num1 + num2)

"-----------Правила наименования переменных-----------"
a = 5  # можно, но назначение не понятно
# 1num = 10   нельзя начинать названия с чисел
# num-df = 12   нельзя использовать символы кроме _
# hello world = "hello world"   нельзя использовать символы кроме _
# print = 'print'   нельзя называть переменные встроенными названиями
# if = 2   нельзя называть переменные ключевыми словами

# Snake Case - python стиль наименования переменных
hello_world = 'Hello world'

# Camel Case - стиль остальных языков програмирования
helloWorld = 'Hello world'


"======================Ввод и вывод данных======================"
# print - функция вывода данных в терминал
# input - функция ввода данных с терминала

number = input("Введите число: ")
print("Введенное число -", number)

"=========================Типы данных========================="
# Типы данных делятся на 2 вида: изменяемые и неизменяемые
# Изменяемые: list(список), dict(словари), set(множества)
# Неизменяемые: int, float, decimal, complex(числа), str(строка), tuple(кортеж), bool(булевые значения), None(пустота)

list_ = [1, 2, 3, 4]
dict_ = {"a":1, "b":2, "c":3}
set_ = {1, 2, 4, 5}

int_ = 10
float_ = 13.2
str_ = "hello world"
tuple_ = (1, 2, 4, 5)
bool_1 = True
bool_2 = False
none_ = None

print("Изменяемые типы данных:", list_, dict_, set_)
print("Неизменяемые типы данных:", int_, float_, str_, tuple_, bool_1, bool_2, none_)