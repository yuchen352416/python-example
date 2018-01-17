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

    def __str__(self):  # 重写父类方法
        return "Animal(name:{0}, age:{1}) Call....".format(self.__name, self.age)


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


# Python 可以在类的方法内用 self 绑定属性, 也可在类的外部绑定属性

class Dog(Animal):

    def __int__(self, args):
        super(Dog, self).__init__(args)


class Cat(Animal):

    def __int__(self, args):
        super(Cat, self).__init__(args)

dog = Dog({"name":"lucy", "age":2})

cat = Cat({"name":"lola", "age":1})

dog.call()
cat.call()