#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class FileUtils(object):

	def __init__(self, **args):
		super(FileUtils, self).__init__()
		self.file_name = args.get("file_name")

	def read_line(self, mode='r'):
		f = open(self.file_name, mode, encoding="UTF-8")
		result = []
		for line in f.readlines():
			result.append(line.strip())
		return result