"=================================List================================="
# списки - изменяемый, индексируемый, упорядоченный, итерируемый тип данных, предназначенный для хранения любых данных в определенном порядке

list1 = [1, 2, 3, 'hello', [2, 4, 0.4], None, True]
list1[3] # 'hello'
list1[3][-1] # 'o'
list1[-1] # True
list1[4] # [2, 4, 0.4]
list1[4][0] # 2

list2 = list("hello")
# ['h', 'e', 'l', 'l', 'o']

list3 = list(range(1,11))
# [1,2,3,4,5,6,7,8,9,10]

list4 = [1] * 5
# [1,1,1,1,1]


"=====================Методы списков====================="
# append - добавляет элемент в конец списка
list2 = []
list2.append(1)
print(list2) # [1]
list2.append("hello")
print(list2) # [1, 'hello']

# pop - удаляет элемнт из списка по индексу и результатом метода будет удаленный элемент (метод возвращает удаленный элемент), если не передать индекс - удалит с конца
list1 = [1,2,3,4,5,6,7,8]
popped = list1.pop(1)
print(list1, popped)
# [1,3,4,5,6,7,8] 2
popped = list1.pop()
print(list1, popped)
# [1,3,4,5,6,7] 8

# если список пустой, то при удалении выйдет IndexError
list1 = []
list1.pop()
# IndexError: pop from empty list

# если передать не существующий индекс выйдет IndexError
list1 = [1,2,3]
list1.pop(5)
# IndexError: pop index out of range


# remove - удаляет элемент из списка по значению
list2.remove('hello')
print(list2) # []

list3 = [1,2,3,4,1,1,3,2,5]
list3.remove(1)
# [2,3,4,1,1,3,2,5]

# count - считает количество принятого элемента в списке
list4 = [1,2,3,1,2,3,1,1,2,3]
list4.count(1)
# 4

list5 = ['hello', 'hello', 'hello']
list5.count('hello') # 3
list5.count('l') # 0

# index - возвращает индекс первого вхождения прининятого элемента
list6 = ['hello', 10, True, None, 10, 'hello']
list6.index(10) # 1
list6.index('hello') # 0

# insert - добавляет элемент в список по индексу
list7 = ['hello', 15, 'world', True, [1,2,3]]
list7.insert(1, False)
# ['hello', False, 15, 'world', True, [1,2,3]]

# extend - добавляет элементы принятого списка в первый список, изменяя его
list1 = [10,20,30]
list2 = [50,60,70]
list1.extend(list2)
print(list1)
# [10,20,30,50,60,70]
print(list2)
# [50,60,70]

# reverse - изменяет список, расставляя его элементы в обратном порядке
list3 = [1,2,3,4,5,[6,7,8]]
list3.reverse()
print(list3)
# [[6, 7, 8], 5, 4, 3, 2, 1]

# sort - сортирует список, состоящий из элементов одного типа данных
list4 = [4,2,6,2,8,4,0,12,56]
list4.sort()
print(list4)
# [0,2,2,4,4,6,8,12,56]

list5 = ['a', 'c', 'b', 'B', 'A']
list5.sort()
print(list5)
# ['A', 'B', 'a', 'b', 'c']

list6 = [1,2,3,'hello']
list6.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

# reverse=True сортировка по убыванию
list7 = [4,2,6,2,8,4,0,12,56]
list7.sort(reverse=True)
print(list7)
# [56, 12, 8, 6, 4, 4, 2, 2, 0]

# clear - очищает список
list1 = [2,4,6,78,9,0,32]
list1.clear()
print(list1)
# []


# len - считает количество элементов в последовательности
list1 = [1,2,3,[4,5,[6,7,8]]]
len(list1)
# 4




a, b = [2,3]
# a = 2
# b = 3

a, b = [1]
# ValueError: not enough values to unpack (expected 2, got 1)

a, b = [1,2,3]
# ValueError: too many values to unpack (expected 2)

a, b = [1,2,3,4]
# ValueError: too many values to unpack (expected 2)

name, age, prof = ['Nastya', 13, 'Mentor']
# name = 'Nastya'
# age = 13
# prof = 'Mentor'



# enumerate - нумерует последовательность начиная с 0

list4 = ['a', 'b', 'c', 'd']

for i in enumerate(list4):
    print(i)

s = "lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"
res = []
for word in s.split():
    w = word[:-1]
    index = word[-1]
    res.append([w, int(index)])
print(" ".join([x[0] for x in sorted(res, key=lambda x: x[1])]))

            