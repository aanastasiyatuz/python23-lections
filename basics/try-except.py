"======================================Exceptions======================================"
# Исключения (ошибки) - обьекты, которые прерывают работу кода, если не были обработанны

SyntaxError
# исключение, которое выходит, когда в коде допущенна синтаксическая ошибка
"""
(
SyntaxError: unexpected EOF while parsing
(когда мы не закрыли скобочку или кавычку)
"""

"""
a = 
SyntaxError: invalid syntax
(когда мы сделали что-то не правильно в синтаксисе)
"""


NameError
# исключение, которое выходит, когда мы обращаемся к несуществующей переменной
"""
slfdjhuksrgh.split()
NameError: name 'slfdjhuksrgh' is not defined
"""


IndexError
# исключение, которое выходит, когда мы обращаемся по несуществующему индексу
"""
list_ = [1,2,3,4,5]
list_[1000]
IndexError: list index out of range
"""

"""
[1,2,3,4,5].pop(1000)
IndexError: pop index out of range
"""

"""
[].pop()
IndexError: pop from empty list
"""


KeyError
# исключение, которое выходит, когда обращаемся по несуществующему ключу
dict_ = {'a':1}
# dict_['b']  - KeyError: 'b'
# dict_.pop('b')   - KeyError: 'b'

dict_.get('b')
# ошибка не выйдет, просто если ключа нет - вернется None


ValueError
# когда мы передаем в функцию не коректный для нее тип данных
# когда мы распаковываем итерируемый обьект на несколько переменных и кол-во переменных не совпадает с кол-вом элементов в итерируемом обьекте

"""
int('10d')
ValueError: invalid literal for int() with base 10: '10d'
"""

"""
a,b,c = [1,2]
ValueError: not enough values to unpack (expected 3, got 2)
"""


TypeError
# когда мы пытаемся использовать методы не свойственные какому-то типу данных
# или когда мы пытаемся передать функции больше или меньше аргументов, чем принимает функция

"""
for i in 12345678:
    ...
TypeError: 'int' object is not iterable
"""

"""
5 + '5'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
"""

"""
'5' + 5
TypeError: can only concatenate str (not "int") to str
"""

"""
{[1,2,3]:"hello"}
TypeError: unhashable type: 'list'
"""

"""
input('hello', 1)
TypeError: input expected at most 1 argument, got 2
"""

"""
[].append()
TypeError: append() takes exactly one argument (0 given)
"""


ZeroDivisionError
# выходит при делении 0
"""
45 / 0
ZeroDivisionError: division by zero
"""

"""
3 // 0
ZeroDivisionError: integer division or modulo by zero
"""

"""
3 % 0
ZeroDivisionError: integer division or modulo by zero
"""


AttributeError
# выходит, когда мы обращаемся к несуществующему аттрибуту или методу обьекта (типа данных)

"""
[].replace('a', '')
AttributeError: 'list' object has no attribute 'replace'
"""

"""
''.pop()
AttributeError: 'str' object has no attribute 'pop'
"""


IndentationError
# выходит, когда мы не правильно используем отступы
"""
   a = 5
IndentationError: unexpected indent
"""

"""
for i in range(10):
print(i)
IndentationError: expected an indented block
"""


Exception
# исключение, которое создали, чтобы его вызывать



"==============================Вызов исключений=============================="
# raise NameError
# NameError

# raise NameError('Не правильное имя')
# NameError: Не правильное имя



"==============================Обработка исключений=============================="
# чтобы код не прекращал свою работу, мы можем использовать конструкцию try-except, и обрабатывать вызванное исключение

try:
    # код, который возможно вызовет ошибку
    num = int(input("Введите число: "))
except ValueError: # ошибка, которая может возникнуть
    # код который отработает только если ошибка вызвалась
    print("Вы введи не число")
else:
    # код который отработает только если никакая ошибка не вышла
    print("Введенное число", num)
finally:
    # код, который отработает вообще в любом случае
    print("До свидания")

try:
    num = int(input("Введите число"))
except ValueError:
    print("Вы введи не число")
else:
    print("Введенное число", num)
finally:
    print("До свидания")

try:
    raise ValueError
except (SyntaxError, NameError):
    print("Вышла одна из этих ошибок: (SyntaxError, NameError)")

try:
    raise Exception
except:  # отлавливаются все ошибки
    print("Отловленна любая ошибка")

try:
    raise Exception
except Exception: # отлавливаются все ошибки
    print("Отловленна любая ошибка")

try:
    raise TypeError("Type error")
except Exception as error:
    print("Ошибка:", type(error).__name__)
