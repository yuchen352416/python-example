#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging


class MyDict(dict):
	def __init__(self, **kw):
		logging.info("init params ==> %s" % str(kw))
		super(MyDict, self).__init__(**kw)

	def __getattr__(self, item):
		try:
			return self[item]
		except KeyError:
			logging.error(r"MyDict no found [%s]" % item)
			raise KeyError(r"MyDict no found [%s]" % item)

	def __setattr__(self, key, value):
		self[key] = value



