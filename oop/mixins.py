"Миксины - классы, которые будут использоваться для наследования. Но от миксинов не создаются обьекты"

class FlyMixin:
    def fly(self):
        print('я могу летать')

class WalkMixin:
    def walk(self):
        print('я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плыть')

class Human(WalkMixin, SwimMixin):
    name = 'человек'

    def talk(self):
        print('я могу говорить')

class Fish(SwimMixin):
    name = 'рыба'

class Exocoetidae(SwimMixin, FlyMixin):
    name = 'летучая рыба'

class Duck(SwimMixin, WalkMixin, FlyMixin):
    name = 'утка'

objects = [Human(), Fish(), Exocoetidae(), Duck()]

for obj in objects:
    print(obj.name)

    # 'fly' in dir(obj) == hasattr(obj, 'fly')
    attrs = ['fly', 'swim', 'walk', 'talk']
    for attr in attrs:
        if hasattr(obj, attr):
            # attr = 'fly'
            # getattr(obj, attr) == obj.fly
            method = getattr(obj, attr)
            method()

obj = Human()
setattr(obj, 'new_attribute', 'hello world') # obj.new_attribute = 'hello world'
print(dir(obj))
print(obj.new_attribute)

# hasattr - функция, которая принимает обьект и название аттрибута. Возвращает True, если у обьекта есть такой аттрибут (метод)
# getattr - функция, которая принимает обьект и название аттрибута. Возвращает значение аттрибута
# setattr - функция, которая принимает обьект, название аттрибута и значение аттрибута. Добавляет в обьект новый аттрибут или перезапишет одноименный аттрибут.