#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Plant(object):
	name = "植物"

	def __init__(self, *args):
		super(Plant, self).__init__()
		if len(args) > 0:
			self.name = args[0]

	def __str__(self):
		return Plant.name;


pl = Plant("绿萝")
print(pl)
print(pl.name)
delattr(pl, "name")
print(pl.name)


class Cactus(object):
	__slots__ = ("name", "money", "getInfo")

	def __str__(self):
		return self.name


def getCactusInfo(cactus):
	print("这株" + cactus.name + "要" + str(cactus.money) + "美刀")


c = Cactus()
c.name = "沙漠仙人掌"
c.money = 50
c.getInfo = getCactusInfo;
print(c)
c.getInfo(c)


class Lotus(Plant):

	@property
	def colour(self): #
		return self._colour

	@colour.setter
	def colour(self, value):
		print("Assignment ing...")
		self._colour = value

	@property
	def age(self):
		return 54


lotus = Lotus()
lotus.colour = "橙红色" # 调用了 colour()方法
print(lotus.colour)
print(lotus.age)


print(dir(lotus))
print(getattr(lotus, "colour"))
setattr(lotus, "colour", "粉红色") # 调用了 colour()方法
print(getattr(lotus, "_colour"))
setattr(lotus, "_colour", "艳红色") # 没有调用colour()方法
print(lotus.colour)

