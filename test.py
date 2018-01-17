#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Mr.Li'


class Animal(object):

    def run(self):
        print("Animal is running...")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


pig = Animal()
dog = Dog()
cat = Cat()

pig.run()
dog.run()
cat.run()