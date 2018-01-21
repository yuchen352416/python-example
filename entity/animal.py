#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):
    def __init__(self, args):
        super(Animal, self).__init__()
        self.__name = args.get("name")
        self.age = args.get("age")

    def call(self):
        print("Animal(name:{0}, age:{1}) Call....".format(self.__name, self.age));

    def setAnimalInfo(self, *, name, age):
        self.__name = name
        self.age = age

    def getAnimalInfo(self):
        return {"name": self.__name, "age": self.age}

    def __str__(self):  # 重写父类方法
        return "Animal(name:{0}, age:{1})".format(self.__name, self.age)


pig = Animal({})
pig.setAnimalInfo(name="tom", age=2)
pig.call()
pig.age = 3
print(pig.age)
print(pig._Animal__name)  # 不建议这样访问
# print(pig.__name) # AttributeError: 'Animal' object has no attribute '__name'
pig.__name = "jack"  # 这么写是错误的, 虽然Python没有限制
print(pig.__name)  # 实际上就是给 pig 绑了一个新的属性
pig.call()




print("\n\n\n")

# Python 可以在类的方法内用 self 绑定属性, 也可在类的外部绑定属性

class Dog(Animal):
    def __init__(self, args):
        super(Dog, self).__init__(args)

    def call(self):
        # print("Dog(name:{0}, age:{1}) wang....".format(super().__name, super.age));
        print("Dog(name:{0}, age:{1}) wang....".format(super(Dog, self).getAnimalInfo().get("name"),
                                                       self.age));

    def __str__(self):  # 重写父类方法
        # return "Dog(name:{0}, age:{1})".format(super().__name, super.age)
        return "Dog(name:{0}, age:{1})".format(super(Dog, self).getAnimalInfo().get("name"),
                                               self.age)


class Cat(Animal):
    def __init__(self, args):
        super(Cat, self).__init__(args)

    def call(self):
        # print("Cat(name:{0}, age:{1}) miao....".format(self.__name, self.age));
        print("Cat(name:{0}, age:{1}) miao....".format(self.getAnimalInfo().get("name"),
                                                       self.age));

    def __str__(self):  # 重写父类方法
        # return "Cat(name:{0}, age:{1})".format(self.__name, self.age)
        return "Cat(name:{0}, age:{1})".format(self.getAnimalInfo().get("name"),
                                               self.age)


dog = Dog({"name": "lucy", "age": 2})
cat = Cat({"name":"lola", "age":1})

dog.call()
cat.call()

print("pig is Animal", isinstance(pig, Animal))
print("dog is Dog", isinstance(dog, Dog))
print("cat is Cat", isinstance(cat, Cat))
print("dog is Animal", isinstance(dog, Animal))
print("cat is Animal", isinstance(cat, Animal))


print("\n\n\n")

dog.age = 1


def getAnimal(animal):
    print(animal)


getAnimal(pig)
getAnimal(dog)
getAnimal(cat)

print("\n\n\n")


##############################################################################################################

print(type(pig) == Animal)

print(dir(pig))
print(dir(dog))

print(getattr(pig, "__name") if hasattr(pig, "__name") else "404")
print(getattr(dog, "__name") if hasattr(dog, "__name") else "404")

if hasattr(cat, "__name"):
    print(cat.__name)
else:
    setattr(cat, "__name", "tom")

print(cat.__name)

getattr(cat, "call")()


def eat():
    print("eat.... ing.....")


setattr(cat, "eat", eat) # 是将方法绑定到了cat这个对象上, 而非类上. 所以新创建的类, 没有eat方法

cat.eat()

cat2 = Cat({"name":"tom", "age":4})
cat2.call()
cat2.eat()


