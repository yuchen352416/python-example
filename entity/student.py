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
