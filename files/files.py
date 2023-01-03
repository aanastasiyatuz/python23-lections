"===========================Модули и пакеты==========================="
# любой файл с расширением .py - модуль
# пакет - набор модулей (обязательно должен быть файл __init__.py)

"==========================Работа с файлами=========================="
# open - функция, которая открывает файл в определенном режиме
'режимы:'
# r - read (только для чтения)
# w - write (только для записи, каждый раз файл очищается)
# a - append (только для дозаписи, добавляется в конец)
# x - создает файл, но если он существует выйдет ошибка
# b - binary (в бинарном виде)

"-----------------------------Read-----------------------------"
file = open('test.txt', 'r')
# print(dir(file))
print(file.writable()) # False (режим read)
print(file.readable()) # True
print(file.read()) # 'Hello\nWorld\nMakers'
print(file.read()) # '' (потому что каретка находится в конце)
file.seek(0) # перенос каретки на начало
print(file.read()) # 'Hello\nWorld\nMakers' (потому что каретка находится на 0 индексе)
file.seek(5)
print(file.read()) # '\nWorld\nMakers' (потому что каретка находится на 5 индексе)
file.seek(0)
print(file.read(3)) # 'Hel' (читаем 3 символа)
print(file.read(3)) # 'lo\n' (читаем еще 3 символа)

file.seek(0)
print(file.readline()) # 'Hello\n' (читает 1 строку (заканчивается на \n))
print(file.readline()) # 'World\n'
print(file.readline()) # 'Makers'
print(file.readline()) # '' (потому что каретка в конце)

file.seek(0)
print(file.readlines()) # ['Hello\n', 'World\n', 'Makers']

print(file.tell()) # 18
file.seek(0)
print(file.tell()) # 0

file.close()

# open('jrfj.txt', 'r')
# FileNotFoundError: [Errno 2] No such file or directory: 'jrfj.txt'


"-------------------------------Write-------------------------------"
file = open('new_file.txt', 'w')
# если файла нет - создаст его

print(file.readable()) # False (можем только записывать)
print(file.writable()) # True

# если были данные, то они удаляются и записываются новые

file.write('Makers\n')
file.write('Bootcamp\n\n')

file.writelines(['Hello\n', 'World\n'])

file.close()


"-------------------------------Append-------------------------------"
file = open('new_file.txt', 'a')

file.write('New line')
file.seek(0)
file.write('Start') # все равно запишет в конец

file.close()


"========================Контекстный менеджер========================"
# конструкция with

# try:
#     file = open('sjdhf', 'w')
#     file.read() # io.UnsupportedOperation: not readable
# finally:
#     file.close()

with open('test.txt', 'r') as f:
    print(f.read())

print(f.closed) # True - файл закрылся

try:
    file = open('test.txt', 'r')
    print(file.read())
finally:
    file.close()

# конструкция with работает с любыми обьектами у которых есть 2 метода __enter__, __exit__
# __enter__ работает в начале конструкции with (try)
# __exit__ работает когда конструкция закончила работу или вышла ошибка в этой конструкции (finally)


class Test:
    def __enter__(self):
        print("Начало работы")
        return self
    
    def __exit__(self, *a, **kw):
        print("Завершение работы")
    
    def hello(self):
        print("Hello world")

with Test() as test:
    test.hello()
