#!/usr/bin/env python
# -*- coding: utf-8 -*


class Chain(object):
	def __init__(self, method='GET',  path=''):
		super(Chain, self).__init__()
		self._path = path
		self._method = method

	def __str__(self):
		return "{0} {1}".format(self._method, self._path)

	def __getattr__(self, path):
		if path == "user":
			return lambda x: Chain(self._method, "{0}/{1}/{2}".format(self._path, path, x))
		return Chain(self._method, "{0}/{1}".format(self._path, path))


print(Chain("POST").status.user("yuchen352416").timeline.list)
