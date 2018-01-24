#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging, unittest
from utils.FileUtils import FileUtils


class TestFileUtils(unittest.TestCase):

	def test_init(self):
		f = FileUtils(file_name="/Users/smile/Desktop/学习计划.txt")
		print(f.readLine(mode='r'))
		print("hello")


if __name__ == "__main__":
	TestFileUtils().test_init()
