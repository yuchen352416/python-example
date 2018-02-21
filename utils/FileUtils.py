#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

class FileUtils(object):

	def __init__(self, **args):
		super(FileUtils, self).__init__()

	def read(self, file_name, mode='r'):
		"""
		:param file_name: file_path and file_name
		:param mode: open mode
		:return: file content lines array
		"""
		result = []
		if not os.path.exists(file_name):
			print("没有 \"{0}\" 此文件...".format(file_name))
			return None
		with open(file_name, mode, encoding="UTF-8") as f:
			for line in f.readlines():
				result.append(line.strip())
		return result

	def write(self, file_name, content, mode='w'):
		result = False
		with open(file_name, mode, encoding="UTF-8") as f:
			for line in content:
				f.write(line + "\r\n")
			result = True
		return result

	def truncate(self, file_name):
		with open(file_name, "w", encoding="UTF-8") as f:
			f.write("")
		return True



fu = FileUtils()
# result = fu.read("/Users/smile/example.log")
# result = fu.write("/Users/smile/example1.log", result, "a")
result = fu.truncate("/Users/smile/example1.log")
print(result)
