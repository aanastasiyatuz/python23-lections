"Полиморфизм - принцип ООП, в котором в разных классах методы называются одинаково, но реализация разная. (один итерфейс - разный функционал)"

class Dog:
    def speak(self):
        print("гав-гав")

class Cat:
    def speak(self):
        print("мяу-мяу")

class Frog:
    def speak(self):
        print("ква-ква")

objects = [Frog(), Cat(), Dog(), Cat(), Frog(), Dog()]

for obj in objects:
    obj.speak()


print('list', dir(list))
print('dict', dir(dict))

# __add__
print(5 + 5) # int
print('5' + '5') # str
print([1,2,3] + [4,5,6]) # list
a = [1,2,3]
b = [4,5,6]
print(a.__add__(b))

# __len__
print(len('abc')) # 3
print(len(['abc'])) # 1
print(len([[1,2,3],[4,5,6]])) # 2
print('abc'.__len__())

print(globals())