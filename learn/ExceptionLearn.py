#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


def division(x, y):
	if y == 0:
		raise ValueError("除数不能为 0")
	return x / y


try:
	print(division(4, 0))
except ValueError as e:
	# raise 
	print("除数为0, 计算终止....", e)
	logging.exception(e)
else:
	print("计算正常结束....")
finally:
	print("一切终归于平静....")

