# 1. Как узнать путь до текущей директории
# pwd

# 2. Создайте:
# .
# ├── test1
# │   ├── hello
# │   │   └── test.py
# │   ├── test.py
# │   └── test.txt
# └── test2

# mkdir test{1,2}
# mkdir test1/hello
# touch test1/test.{txt,py}
# touch test1/hello/test.py

# 3. Создайте переменную string со значением hello world и переменную num с любым целым числом
string = 'hello world'
num = 6

# 4. Выведите в терминал string в верхнем регистре
print(string.upper())

# 5. Запросите у пользователя число, выведите в теминал остаток от деления num на это число
num2 = int(input())
print(num2 % num)

# 6. Выведите в терминал четное ли число, которое запросили
print(not num2 % 2)

# 7. Выведите 3й символ строки string
print(string[2])

# 8. Создайте переменную text с данным текстом:
# Maker's Bootcamp
# Добро пожаловать в "Makers.kg"
# Здесь исполняются мечты.
text = """
Maker's Bootcamp
Добро пожаловать в "Makers.kg"
Здесь исполняются мечты.
"""

# 9. Выведите кол-во символов в text
print(len(text))

# 10. Выведите только вторую строку text
print(text.split("\n")[1])