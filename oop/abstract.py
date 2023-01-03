"Абстракция - принцип ООП, в котором создается класс-пустышка, где задаются названия аттрибутов и методов, для того, чтобы в дочерних классах не забыть их перепределить."

from abc import ABC, abstractmethod, abstractproperty

class AbstractAnimal(ABC):
    @abstractproperty
    def legs(self):
        ...

    @abstractmethod
    def voice(self):
        ...

# obj = AbstractAnimal()
# TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

class Dog(AbstractAnimal):
    ...

# obj = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice

class Dog(AbstractAnimal):
    def voice(self):
        print("гав-гав")

# obj = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract methods legs

class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print("гав-гав")

obj = Dog()
obj.voice() # гав-гав
print(obj.legs) # 4

class Cat(AbstractAnimal):
    legs = 4

# obj = Cat()
# TypeError: Can't instantiate abstract class Cat with abstract methods voice
