# # Big O notation
# nums = [1,2,3,4] # n = 4
# target = 5

# for i in nums: # O(n)
#     if i == target:
#         print(i)

# for i in nums: # O(n)
#     if i == target:
#         print(i)
#         break

# # O(1)
# nums = [1,2,3,4,5] # 5
# print(nums[0]) # 1
# print(nums[4]) # 1
# print(nums[5]) # 1 IndexError

# dict_ = {'a':1}
# print(dict_['a']) # 1

# # O(n)
# nums = [1,2,3,4] # n = 4
# for i in nums:
#     print(i) # 4 раза

# # O(n2)
# nums = [1,2,3,4]
# for i in nums: # 4 раза
#     for j in nums: # еще по 4 раза
#         print(i, j) # 16 раз = 4**2

# # O(log n)
# nums = list(range(1000000000))
# target = 1000000000
# count = 0

# while nums:
#     count += 1
#     mid = len(nums) // 2
#     if target == nums[mid]:
#         print("число", target) # нашли
#         break
#     elif target > nums[mid]:
#         nums = nums[mid+1 :] # срезаем правую часть
#     elif target < nums[mid]:
#         nums = nums[: mid] # срезаем левую часть
# print(count)



# Структуры данных

# stack - LIFO
stack = [1,2,3,4,5]
stack.append(6) # добавление в конец
stack.pop() # удаление с конца

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

stack = Stack()
stack.push(1) # добавляет в конец
stack.push(2) # добавляет в конец
stack.pop() # удаляет с конца


# queue - очередь FIFO
queue = [1,2,3,4]
queue.pop(0) # удаляем с начала списка
queue.append(5) # добавляем в конец

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


# Linked List
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

linked_list = ListNode("hello")
linked_list.next = ListNode(2)
linked_list.next.next = ListNode(3)
linked_list.next.next.next = ListNode(4)
linked_list.next.next.next.next = ListNode(5)

"обход linked list"
# print(linked_list.value)
# print(linked_list.next.value)
# print(linked_list.next.next.value)
# print(linked_list.next.next.next.value)

temp = linked_list # в самом начале
while temp:
    print(temp.value)
    temp = temp.next


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