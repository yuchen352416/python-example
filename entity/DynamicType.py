#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类


def fn(self, name):
	self._name = name


def hell(self):
	print("Hello %s" % self._name)


Hello = type("Hello", (object,), {"hello": hell, "setName": fn})

hello = Hello()
hello.setName("Jack")
hello.hello() # Hello Jack
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass
# metaclass是类的模板，所以必须从`type`类型派生：


class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
	pass


L = MyList()
L.add(1)
print(L)
