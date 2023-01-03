"===================================Строки==================================="
# строки - неизменяемый тип данных, который предназначен для хранения текста (последовательности символов), заключенного в одинарные или двойные кавычки

string1 = 'строка с одинарными кавычками'
string2 = "строка с двойными кавычками"
# error = 'не правильная строка"
string3 = "Don't"  # внутри двойных кавычек все одинарные - просто символы
string4 = ' "Makers bootcamp" '  # внутри одинарных кавычек все двойные - просто символы

string5 = '''
Многострочный текст
в одинарных кавычках
Тут можно ставить "любые" 'кавычки'
'''

string6 = """
Многострочный текст
в двойных кавычках
Тут можно ставить "любые" 'кавычки'
"""

string7 = 'hello' + ' ' + 'world'
# 'hello world'

string8 = 'A' * 8
# 'AAAAAAAA'


"==========================Экранизация строк=========================="
'\n' # перенос на новую строку
print('hello\nworld')
# hello
# world

'\t' # табуляция
print('hello\tworld')
# hello   world

'\'' # отображение '
"\"" # отображение "
print('Don\'t')
# Don't

'\\' # отображение \
print('\\t - табуляция')
# \t - табуляция

'\v' # перенос на новую строку со смещением вправо на длину предыдущей строки
print('hello\vworld\vmakers\vbootcamp')
# hello
#      world
#           makers
#                 bootcamp

'\r' # перенос каретки на начало строки
print('Hello world\rHi')
# Hillo world


"====================Форматирование строк===================="
title = 'iPhone 14'
price = 150
format1 = f'Название: {title}\nЦена: {price}'
print(format1)
# Название: iPhone 14
# Цена: 150

format2 = 'Название: {}\nЦена: {}'
print(format2.format("Хлеб", 28))
print(format2.format("Человек", 200))
# print(format2.format('sdfukgh'))
# IndexError: Replacement index 1 out of range for positional args tuple

format3 = 'Название: %s\nЦена: %s'
print(format3 % ('iphone', 345))


"==========================Методы строк=========================="
# методы - функции, которые относятся к определенному классу (типу данных), к ним мы обращаемся через точку

dir(str)  # посмотреть все методы класса

'HeLLo'.lower() # 'hello'
'HeLLo'.upper() # 'HELLO'
 
'HeLLo'.swapcase() # 'hEllO'
'hello world'.title() # 'Hello World'
'hello world'.capitalize() # 'Hello world'

'hello'.center(11) # '   hello   '
'hello'.center(11, '-') # '---hello---'

'hello world'.count('l') # 3
'hello world'.count('ll') # 1
'hello world'.count('makers') # 0

'hello world'.startswith('hello') # True
'hello world'.startswith('H') # False
'hello world'.endswith('ld') # True

'hello world'.islower() # True
'Hello world'.islower() # False
'HELLO'.isupper() # True
'1233'.isdigit() # True
'hello'.isalpha() # True
'hello 1'.isalpha() # False
'hello'.isalnum() # False
'12345'.isalnum() # False
'h1'.isalnum() # True

'hello world'.split() # ['hello', 'world']
'hello world'.split('o') # ['hell', ' w', 'rld']
'hello world'.split('makers') # ['hello world']

'-'.join(['hello', 'world']) # 'hello-world'
' '.join(['hello', 'world']) # 'hello world'
''.join(['hello', 'world']) # 'helloworld'

string1 = '                        12   hello             '
string1.strip() # '12  hello'

string2 = '$sdjkfh#dfgh$xfukgh$$$$'
string2.strip('$') # 'sdjkfh#dfgh$xfukgh'

string1.lstrip() # '12   hello             '
string1.rstrip() # '                        12   hello'


"==========================Индексы=========================="
# индекс - порядковый номер элемента в последовательности (символа в строке) (индексация начинается с 0)

'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#             ... -2 -1

string = 'hello world'
string[0] # 'h'
string[10] # 'd'
string[5] # ' '
string[-1] # 'd'

# срез - подстрока строки
string[0:5] # 'hello'
string[0:4] # 'hell'
string[6:10] # 'worl'
string[6:-1] # 'world'
string[6:] # 'world'
string[:5] # 'hello'
string[:] # 'hello world'

string[::2] # 'hlowrd'
string[1:5] # 'ello'
string[1:5:2] # 'el'
string[::-1] # 'dlrow olleh'
string[::-2] # 'drwolh'

immutable_string = 'Hello'
print(immutable_string.upper()) # 'HELLO'
print(immutable_string) # 'Hello'
