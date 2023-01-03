"=========================================Comprehensions========================================="
# генератор, с помощью которого мы можем создавать последовательности используя цикл for в одну строку

# результат for элемент in последовательность
# результат for элемент in последовательность if фильтр

comprehension = (i for i in range(1, 6))
# <generator object <genexpr> at 0x7f9328391a50>
# генератор - итерируемый обьект, который не хранит в себе полностью всю последовательность данных, а создает их когда требуется

print(next(comprehension)) # 1
print(next(comprehension)) # 2
print(next(comprehension)) # 3
print(next(comprehension)) # 4
print(next(comprehension)) # 5
# print(next(comprehension)) # StopIteration

# next - функция, которая запрашивает у генератора текущий элемент и генератор создает следующий элемент


"========================================Синтаксический сахар========================================"
# list comprehension
list_comprehension = list( (i**2 for i in range(1, 6)) )
# [1,4,9,16,25]

list_comprehension2 = [i**2 for i in range(1,6)]
# [1,4,9,16,25]

"Создайте список состоящий из четных чисел от 1 до 10 используя comprehension"
list1 = [i for i in range(2, 11, 2)]
list2 = [i for i in range(1,11) if i % 2 == 0]

list3 = []
for i in range(1, 11):
    if i % 2 == 0:
        list3.append(i)

"Создайте список состоящий из 5 строк 'hello' используя comprehension"
# ['hello', 'hello', 'hello', 'hello', 'hello']
list1 = []
for _ in range(5):
    list1.append('hello')

list2 = ['hello' for _ in range(5)]
list3 = ['hello']*5


"Создать список состоящий из чисел от 1 до 10, но вместо чисел написать 'четное' или 'нечетное'"
list1 = []
for i in range(1,11):
    if i % 2 == 0:
        list1.append('четное')
    else:
        list1.append('нечетное')

list2 = []
for i in range(1,11):
    list2.append('четное' if i % 2 == 0 else 'нечетное')

list3 = [ 'четное' if i % 2 == 0 else 'нечетное' for i in range(1,11) ]

# ['нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное', 'нечетное', 'четное']


"создать список из существующего списка, оставив только строки"
list1 = [1, 'hello', 2, 'a', 2.3, 1000, 'makers']
# ['hello', 'a', 'makers']

list2 = []
for i in list1:
    if type(i) == str:
        list2.append(i)

list3 = [i for i in list1 if type(i) == str]


"======================================Dict comprehension======================================"
dict1 = dict( (i, i**2) for i in range(10) )
dict2 = { i: i**2 for i in range(10) }
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


"Дан словарь, создайте его копию с помощью comprehension"
dict1 = {"a":1, "b":2, "c":3}
dict2 = { key:value for key, value in dict1.items() }
# {"a":1, "b":2, "c":3}

"Дан словарь, поменяйте ключи со значениями с помощью comprehension"
dict1 = {"a":1, "b":2, "c":3}
dict2 = { value:key for key, value in dict1.items() }
# {1:"a", 2:"b", 3:"c"}

"Дан словарь, где значения - списки с числами, созайте словарь, где значениями будут суммы этих списков"
dict1 = {
    "a":[1,2,3,4],
    "b":[10,15,16,17],
    "c":[1,2,54]
}
dict2 = { key:sum(value) for key, value in dict1.items() }
# {"a":10, "b":58, "c":57}

"Создате словарь с ключами - числа 1 до 10, а значения числа в виде строк"
# {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10'}
dict1 = { i:str(i) for i in range(1, 11) }


"Даны 2 списка, создайте словарь, ключами будут элементы из первого списка, значениями - элементы второго списка"
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

dict1 = {}
for ind in range(len(list1)):
    key = list1[ind]
    value = list2[ind]
    dict1[key] = value

dict2 = { list1[ind]:list2[ind] for ind in range(len(list1)) }

dict3 = dict(zip(list1, list2))


"===============================Вложенные comprehension==============================="
"Создайте словарь, где ключами будут числа от 1 до 5, а значениями - списки с числами от 1 до этого числа"
# {1:[1], 2:[1,2], 3:[1,2,3], 4:[1,2,3,4], 5:[1,2,3,4,5]}

dict1 = {}
for i in range(1,6):
    key = i
    value = [j for j in range(1, i+1)]
    dict1[key] = value

dict2 = { i: [j for j in range(1, i+1)] for i in range(1,6) }
dict3 = { i: list(range(1, i+1)) for i in range(1,6) }

"создать список, состоящий из 10 списков, в которых строка 'hello world' повторяется по 5 раз"

list1 = []
for i in range(10):
    inner_list = []
    for j in range(5):
        inner_list.append('hello world')
    list1.append(inner_list)

list2 = [['hello world' for j in range(5)] for i in range(10)]
list3 = [['hello world']*5 for i in range(10)]
list4 = [['hello world']*5]*10

"Создать список, состоящий из 10 списков,в которых будут числа от 1 до 5"
# [[1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5],
# [1,2,3,4,5]]

list1 = [[j for j in range(1,6)] for i in range(10)]
list2 = [list(range(1,6)) for i in range(10)]
list3 = [list(range(1,6))]*10

"Создайте словарь, где ключами будут числа от 1 до 5, а значениями словари, в которых ключами будут числа от 1 до этого числа, а значениями будут списки от 1 до этого числа"
# {
#     1:{
#         1:[1]
#     },
#     2:{
#         1:[1],
#         2:[1,2]
#     },
#     3:{
#         1:[1],
#         2:[1,2],
#         3:[1,2,3]
#     },
#     4:{
#         1:[1],
#         2:[1,2],
#         3:[1,2,3],
#         4:[1,2,3,4]
#     },
#     5:{
#         1:[1],
#         2:[1,2],
#         3:[1,2,3],
#         4:[1,2,3,4],
#         5:[1,2,3,4,5]
#     }
# }

dict1 = {}
for i in range(1,6):
    inner_dict = {}
    for j in range(1, i+1):
        list_ = []
        for k in range(1, j+1):
            list_.append(k)
        inner_dict[j] = list_
    dict1[i] = inner_dict


dict2 = { 
    i:{
        j:[k for k in range(1,j+1)] for j in range(1,i+1)
    } 
    for i in range(1,6)
}
dict3 = {i: {j: [k for k in range(1,j+1)] for j in range(1, i+1)} for i in range(1,6)}
dict4 = {i: {j: list(range(1,j+1)) for j in range(1, i+1)} for i in range(1,6)}

list1 = [
    ["hello", 1, "a", 343, 3.21],
    ["world", 1, "a", 32.1],
    [1, "b", 3, 54],
    [1,2,3,4,5]
]
list2 = [i for list_ in list1 for i in list_  if type(i) == int]
list2 = [i for inner_list in list1 for i in inner_list if type(i) == int or type(i) == float]

# Дан словарь:
dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# Создайте словарь dict2:
# - Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
# - Значением должно быть количество повторений символа 'i' в этом ключе

dict2 = { k.replace('i', ''):k.count('i') for k in dict1}
print(dict2)


# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3
dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}

ids = []

for inner_dict in dict_.values():
    comments = inner_dict['comments']
    if len(comments) > 3:
        for comment in comments:
            ids.append(comment['id'])

ids = [comment['id'] for inner_dict in dict_.values() for comment in inner_dict['comments'] if len(comments) > 3]
