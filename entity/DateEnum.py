#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量
for k, v in Month.member_map_.items():
	print(k, v, v.value)

# value属性则是自动赋给成员的int常量，默认从1开始计数。
print(Month.Jan.value)
print(Month(2))


@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6


print(Weekday(2))
# 自定义value
# @unique装饰器可以帮助我们检查保证没有重复值。

# 单例


class DateUtil(Enum):
	class DateUtil(object):
		def __str__(self):
			return "单例...."

	instance = DateUtil()


print(DateUtil.instance.value)
