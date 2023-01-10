# Стуктуры данных

> Часто используемые структуры данных, которые вы еще не знаете:
> * Hash table
> * Stack
> * Queue
> * Linked list
> * Tree

> Есть конечно и другие, но мы их рассматривать не будем

## Hash Table
> В целом это просто питоновский словарь. Если так взять, то хэш таблица - это структура в которой данные хранятся в парах (ключ-значение)

## Stack
> Куча - это упорядоченная последовательность элементов, в которой элементы добавляются в конец и удаляются с конца. Тоесть следует принципу LIFO (last in - first out). Что зашло последнее - уйдет первое. Причем каждое действие должно выполняться за O(1).

> В python можно найти аналоги stack. Например (list, Collections.deque, queue.LifoQueue). Но нужно заметить, что в list мы можем добавлять элементы в начало или по индексу, а так же удалять по индексу.

> Можно попробовать реализовать кучу (это просто пример, каждый может реализовать ее по разному)

> Самое главное, чтобы в stack были методы:
> * is_empty - возвращает не пустой ли список
> * size (lenght) - возвращает длину кучи
> * top (peek) - возвращает последний элемент
> * push (append) - добавляет элемент в конец
> * pop - удаляет элемент с конца

```py
# это просто одна из реализаций, которую я придумала
class Stack:
    def __init__(self):
        self.size = 0
        self._items = []
    
    def is_empty(self):
        return self.size == 0
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._items[-1]
    
    def push(self, value):
        self._items.append(value)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Pop from an empty stack")
        self.size -= 1
        return self._items.pop()
```

## Queue
> Очередь - это упорядоченная последовательность элементов, в которой элементы добавляются в начало, а удаляются с конца. Тоесть следуют принципу FIFO (first in - first out). Как и в очереди, кто первый пришел, тот первый покинет очередь.

> Также в python можно найти аналоги queue. Например (list, Collections.deque, queue.Queue). 

> Я так же сделаю свой пример для реализации queue.

> В Queue должны быть методы:
> * max_size - максимальная длина очереди (при создании задается)
> * enqueue (add) - добавление элемента в начало
> * dequeue (pop, remove) - удаление элемента с конца
> * front (first) - получение первого элемента в очереди (тот, который первый уйдет при удалении)
> * rear (last) - получение последнего элемента (был добавлен последним)

```py
class Queue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self._items = []
    
    def add(self, value):
        if self.size == self.max_size:
            raise Exception("Queue is full")
        self._items.insert(0, value)
        self.size += 1
    
    def pop(self):
        if self.size == 0:
            raise Exception("Pop from an empty queue")
        self.size -= 1
        return self._items.pop()
    
    def front(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        return self._items[-1]
    
    def rear(self):
        if self.size == 0:
            raise Exception("Queue is empty")
        return self._items[0]
```

## Linked list
> Это почти как список, но немножко сложнее, потому что тут элементы - это отдельные обьекты, и чтобы получить следующий элемент, нужно обратьтся к аттрибуту next у предыдущего элемента

```py
# самое распространенное создание linked list
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
linked_list = ListNode(1, node2)

# в данном случае у нас есть linked_list, у которого в аттрибуте next лежит ссылка на следующий элемент в списке (node2)
# у node2 в аттрибуте next лежит ссылка на следующий элемент в списке (node3)
# и т.д
```

```py
# я попробую сделать класс Linked list (обычно реализация заканчивается на уровне ListNode)
class LinkedList:
    def __init__(self, value):
        self.root = ListNode(value) # начало
        self.tail = self.root # конец (пока тоже начало)
        self.size = 1
    
    def add(self, value):
        self.tail.next = ListNode(value) # у последнего элемента next ставим новый node
        self.tail = self.tail.next # теперь новый node - последний элемент
        self.size += 1
    
    def search(self, value):
        temp = self.root # берем начало списка
        while temp: # проходимся по элементам пока не дойдем до конца
            if temp.value == value:
                return temp # если нашли

            temp = temp.next # берем следующий элемент (у последнего next=None, поэтому цикл завершится)
        return None # если не нашли
    
    def pop(self, index):
        if self.size <= index:
            raise Exception("Index out of range")

        if index == 0: # если удаляем первый элемент
            self.root = self.root.next
            self.size -= 1
            return

        count = 1 # будем считать, сколько уже прошли, берем не 0, потому что если был 0, то он уже отработал выше
        temp = self.root
        while temp:
            if count == index:
                temp.next = temp.next.next # задаем у текущего node следующим элементом node, который стоит через 1 (типо удалили следующий)
                
                if self.size-1 == index:
                    self.tail = temp # если мы удалили последний элемент, то tail ставим последний элемент
                
                self.size -= 1
                return
            temp = temp.next
            count += 1
```

## Tree
> В целом дерево строится по такой же логике, как и LinkedList, только у него есть не один next, а целый список из детей. У дерева есть один корень.

### Binary Tree
> Думаю легче будет начать с двоичного дерева. Потому что у него у каждого узла может быть только 2 ребенка и мы их можем записать не в список, а в аттрибуты left, right.

```py
# один из самых распространенных способов создания бинарного дерева
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left # ссылка на дочерний узел слева
        self.right = right # ссылка на дочерний узел справа

node1 = TreeNode(5)
node2 = TreeNode(6)
node3 = TreeNode(2, node1, node2)
node4 = TreeNode(3)
tree = TreeNode(1, node3, node4)
# понимаю, что сложно это понять, это будет выглядеть так:
```
![alt тут должна быть фотка](https://static.javatpoint.com/ds/images/binary-tree.png)

> Как проходить по бинарному дереву, сначала не хотела писать. но пока пыталась найти хорошую статью, поняла, что везде примеры с лишним кодом, который может запутать в и так не простой теме. Так что вот пример. **Предупреждаю**, тут используется рекурсия, поэтому попробуйте сначала почитать про рекурсию `https://pythonru.com/osnovy/rekursiya-python`

```py
# создадим дерево, как на фотке, но чуток по другому методу (может так понятнее будет)
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(5)
tree.right.right = TreeNode(6)

# создадим функции, которые будут обходить все элементы дерева и выводить их значения
# тут нужно знать что есть 3 вида обхода деревьев
# 1. прямой обход - когда мы идем сверху вниз (от корня) (1-2-5-6-3)
# 2. обратный обход - когда мы идем снизу вверх (5-6-2-3-1)
# 3. центрированный обход - когда мы идем слева направо (5-2-6-1-3)

def pre_order(node):
    # прямой обход
    if node: # если он не None
        print(node.value) # сначала выводим значение родителя
        pre_order(node.left) # идем за его левым ребенком
        pre_order(node.right) # идем за его правым ребенком

pre_order(tree) # 1 2 5 6 3


def post_order(node):
    # обратный обход
    if node:
        post_order(node.left) # сначала идем за его левым ребенком
        post_order(node.right) # потом идем за его правым ребенком
        print(node.value) # и только потом выводим значение родителя

post_order(tree) # 5 6 2 3 1


def in_order(node):
    # центрированный обход
    if node:
        in_order(node.left) # сначала идем за его левым ребенком
        print(node.value) # потом выводим значение родителя
        in_order(node.right) # и только потом идем за его левым ребенком

in_order(tree) # 5 2 6 1 3
```

### Binary Search Tree
> В целом тоже самое, что и просто бинарное дерево, но оно используется для поиска, поэтому значения в нем устанавливаются так: значение, которое меньше родителя будет в его левой части, а значение, которое больше родителя - в правой.

![alt тут должна быть фотка](https://www.w3resource.com/w3r_images/python-binary-search-tree-image-exercise-1.svg)

> Проход по такому дереву точно такой же, поэтому давайтя тут я покажу поиск по этому дереву. Если число меньше текущего узла, то будем двигать влево, если больше - вправо.
```py
# создадим дерево как на фотке
btree = TreeNode(4)
btree.left = TreeNode(2)
btree.right = TreeNode(6)
btree.left.left = TreeNode(1)
btree.left.right = TreeNode(3)
btree.right.left = TreeNode(5)
btree.right.right = TreeNode(7)

# создадим функцию для поиска
def search(node, target):
    if not node: # если мы дошли до конца, но так и не нашли
        return None

    if node.value == target: # если нашли, возвращаем этот node
        return node

    if node.value > target: # если искомое число меньше, идем в левую часть
        return search(node.left, target) # возвращаем результат поиска в левой части

    if node.value < target: # если больше - в правую
        return search(node.right, target) # возвращаем результат поиска в правой части
```

### Tree
> Возвращаясь к обычным деревьям, у узлов которых может быть много детей

> Создадим другой класс, для создания такого дерева

```py
# опять же просто пример того, как это реализовала бы я
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add(self, *children):
        for child in children:
            self.children.append(TreeNode(child))
```

![alt тут должна быть фотка](https://s3.amazonaws.com/devcamp-publishing/algorithms/002-data-structures/tree-data-structure-types/Slide4.png)

```py
# создадим дерево как на фотке
tree = TreeNode(42)
tree.add(29, 89)
tree.children[0].add(1, 1, 35)
```

> Давайте просто пройдемся по нему и выведем все его значения

```py
def walk(node):
    if node:
        print(node.value)
        if node.children: # если есть дети
            for child in node.children: # проходимся по каждому из детей
                walk(child)

walk(tree)
# 42 29 1 1 35 89
```