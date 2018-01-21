#!/usr/bin/env python
# -*- coding: utf-8 -*


class CustomMade(object):

	def __init__(self, *path):
		super(CustomMade, self).__init__()
		self.index = 0

	def __str__(self):
		return "我被主人改了toString方法"

	def __repr__(self):
		return "我也被主人改了toString方法"

	def __iter__(self):
		return self

	def __next__(self):
		self.index += 2
		if self.index > 100:
			raise StopIteration()
		return self.index

	def __getitem__(self, item):
		if isinstance(item, int):
			if item > 50 or item < -50:
				raise IndexError()
			else:
				if item < 0:
					item = 50 + item
				index = 2
				for x in range(item):
					index += 2
				return index

		if isinstance(item, slice):
			start = item.start
			stop = item.stop
			step = item.step
			if start is None:
				start = 0
			if step is None:
				step = 1
			if start < 0:
				start = 50 + start
			if stop < 0:
				stop = 50 + stop
			result = []
			index = 2
			skip = -1
			for x in range(stop):
				if x >= start:
					skip += 1
					if skip % step == 0:
						result.append(index)
				index += 2
			return result


cm = CustomMade()
print(cm)
for x in cm:
	print(x)

print(cm[1])
print(cm[:10:2])
