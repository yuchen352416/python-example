#!/usr/bin/env python
# -*- coding: utf-8 -*


class Student(object):
	def __init__(self, name):
		super(Student, self).__init__()
		self._name = name

	def __call__(self, *args, **kw):
		print("Student name is %s" % self._name)


s = Student('Jack')
s()
