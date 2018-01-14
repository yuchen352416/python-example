#1
# print("Hello Python...")
# print("Guess....")
# t1 = input()
# t2 = t1
# print("input text is", t1)
# t2 = t2 + "---new"
# print("change text is", t2)
# print("input text is", t1)

#2
# print(1024 * 768)
# num1 = input("input number :")
# num2 = input("input number :")
# sum = int(num1) + int(num2)
# print(num1, '+', num2, '=', sum)

#3
# print('I\'m "OK"!')
# print('''\\\n
# \t
# \"
# \'''')

#4
# a = "xyz"
# b = "xyz"
# print(a == b) # True
# a = "abc"
# b = "abcd"
# print(b > a) # True
# a = "abd"
# b = "abcd"
# print(b > a) # False
# t1 = True
# t2 = False
# t3 = t1 and t2 # false
# t4 = t1 or t2 # true
# t5 = not ((t1 and t2) or t3) # true
# print("t1", t1)
# print("t2", t2)
# print("t3", t3)
# print("t4", t4)
# print("t5", t5)
# try:
# 	age = int(input("input age:"))
# 	if age >= 18: {
# 		print("major")
# 	}
# 	else: {
# 		print("nonage")
# 	}
# except Exception as e:
# 	print("Error input age not number!")

#5
# Python 本身为动态语言, 变量的数据类型不会是固定的
# age = 30
# height = 1.78
# name = "Tom"
# flag = True
# print("age =", age, "\t\t Type:", type(age))
# print("height =", height, "\t\t Type:", type(height))
# print("name =", name, "\t\t Type:", type(name))
# print("flag =", flag, "\t\t Type:", type(flag))
# a = "xyz"
# b = a	# 这个操作, 实际上是把 "xyz" 所在的内存地址, 赋值给了 b
# a = "abc"	# 把 "abc" 所在的内存地址, 赋值给 a 
# print("a =", a) # abc
# print("b =", b) # xyz
# PI = 3.14159265339
# print(PI)
# print(10 / 3) # 3.3333333333333335
# print(9 / 3) # 3.0
# print(10 // 3) # 3 (整除)
# print(10 % 3) # 1 (取余)

#6
# code = ord("A") # 65
# char = chr(code + 32)
# print(code)
# # print(char)
# code = ord("森") # 26862
# char = '\u0041' # A 
# char = '\u68EE' # \u 后表示十六进制的一个数
# print(code)
# print(char)
# -------------------------------------------------------
# x = b'A'
# y = 'A'
# print('x =', x, '\t' ,type(x)) # <class 'bytes'>
# print('y =', y, '\t' ,type(y)) # <class 'str'>
# z = ord(x) 
# print(z) # 65
# -------------------------------------------------------
# print('A'.encode('ASCII'))
# print('森'.encode('GBK')) # b'\xc9\xad'
# print('森'.encode('GB2312')) # b'\xc9\xad'
# print('森'.encode('UTF-8')) # b'\xe6\xa3\xae'
# -------------------------------------------------------
# b'\xc9 \xad' => 11001001 10101101
# b'\xe6\xa3\xae' => 11100110 10100011 10101110
# x = b'A'
# print(x)
# print(x.decode("ASCII"))
# print(x.decode("GB2312"))
# print(x.decode("GBK"))
# print(x.decode("UTF-8"))
# -------------------------------------------------------
# x = b'\xc9\xad'
# print(x)
# print(x.decode("GBK"))
# print(x.decode("GB2312"))
# print(x.decode("UTF-8")) # utf-8占用三个字节, 而x却是两个字节, 所以这里是不对的
# print(b'\x41'.decode("ASCII"))
# print(b'\xe6\xa3\xae'.decode("UTF-8"))
# # ignore error
# print(x.decode("ASCII", errors='ignore'))
# print( b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
# -------------------------------------------------------
# print(len('ABC')) # 3
# print(len('森A')) # 2
# x = b'\xc9\xad' 
# print(x) 
# print(x.decode("GBK")) # 森
# print(len(x)) # 2
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
# print(len('森'.encode('utf-8'))) # 3
# print(len('森A'.encode('utf-8'))) # 4
# -------------------------------------------------------
# 我们通常在文件开头写上这两行
# 1. #!/usr/bin/env python3  # 告诉Linux/OS X系统，这是一个Python可执行程序
# 2. # -*- coding: utf-8 -*- # 告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

#7 字符串格式化
# s = 'Hello %s' % ('World!')
# print(s)
# %d 表示 整数
# %f 表示 浮点数
# %s 表示 字符串
# %x 表示 十六进制整数
# s = 'Age: %s. Gender: %s' % (25, True)
# s = 'Age: %d. Gender: %s' % (25, True)
# s = 'Age: %f. Gender: %s' % (25, True)
# s = 'Age: %x. Gender: %s' % (25, True) # 十进制25传入, 会转化一次, 变为十六进制的 19 
# print(s)
# s = 'Growth rate: %d%%' % (7) # 在使用格式化占位符的字符串中, 用 %% 来表示一个 %  
# print(s)
# -------------------------------------------------------
# 使用format方法, 格式化输出
# s =  'Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125)
# print(s)
# -------------------------------------------------------
# r = (85 - 72) / 72 * 100
# print('小明今年的成绩比去年提升了 {0:.1f}%'.format(r))
# print('小明今年的成绩比去年提升了 %.1f %%' % (r))

#8
# arr = [["A", "B", "C"], ["I", "J", "K"], ["X", "Y", "Z"]]
# for i in range(len(arr)):
# 	for j in range(len(arr[i])):
# 		print("%s(%d, %d)" % (arr[i][j], i + 1, j + 1))
# 	print()
# arr[1].pop(-2) # ['I', 'K']
# arr[1].pop() # ['I']
# arr[1].append("T") # ['I', 'T']
# arr[1].insert(2, "M") # ['I', 'T', 'M']
# arr[1][1] = "N" # ['I', 'N', 'M']
# print(arr[1])
# -------------------------------------------------------
# classmates = ('Michael', 'Bob', 'Tracy')
# print('classmates =', classmates)
# print('len(classmates) =', len(classmates))
# print('classmates[0] =', classmates[0])
# print('classmates[1] =', classmates[1])
# print('classmates[2] =', classmates[2])
# print('classmates[-1] =', classmates[-1])
# cannot modify 3:
# classmates[0] = 'Adam'  # 元组, 不允许修改

#9
# while (True):
# 	try:
# 		height = float(input("请输入您的身高:"))
# 		weight = float(input("请输入您的体重:"))
# 		break
# 	except Exception as e:
# 		print("您输入的数据有问题, 请重新输入.")
# bmi = weight / (height * height)
# if bmi > 32:
# 	print("严重肥胖!")
# elif bmi > 28 and bmi <= 32:
# 	print("肥胖")
# elif bmi > 25 and bmi <= 28:
# 	print("过重")
# elif bmi > 18.5 and bmi <= 25:
# 	print("正常")
# else: 
# 	print("过轻")

# x = 0 # False
# x = 1 # True
# x = -1 # True
# x = () # False
# x = (1, ) # True
# x = '' # False
# x = None # False
# if x:
# 	print("True")
# else:
# 	print("False")
# -------------------------------------------------------
# foo = "ABC"
# print(foo.__eq__("ABc"))
# num = 1.0
# if isinstance(num, float):
# 	print("num is float")

#10
# names = ['Michael', 'Bob', 'Tom', 'Tracy']
# for name in names:
# 	if not (name == "Tom") :
# 		print(name)
# 	else :
# 		continue
# -------------------------------------------------------
# for i in range(1,10):
# 	print(i)
# -------------------------------------------------------
# arr = list(range(1, 10))
# print(arr)
# -------------------------------------------------------
# n = 10;
# while n > 0:
# 	n -= 2
# 	print(n)

#11
# dictionary = {
# 	"name" : "小明", 
# 	"age" : 23, 
# 	"phone":"18733778565",
# 	"age" : 24 # 这样是可以的, 新值会覆盖旧值, 但实际情况中这样没有意义
# }
# dictionary["age"] = dictionary["age"] + 1
# dictionary["address"] = "北京, 丰台区"
# print(isinstance(dictionary["phone"], str))
# print(isinstance(dictionary["age"], int))
# print(isinstance(dictionary["name"], str))
# print(dictionary["age"])
# if "age" in dictionary:
# 	print(dictionary["age"])
# for key in dictionary:
# 	print(key, '\t => \t', dictionary[key])
# print(dictionary.pop("age"))
# print(dictionary.get("Age")) # None
# # print(dictionary["Age"]) # KeyError: 'Age'
# print(dictionary.get("Age", -1)) # -1, 若Map中没对应的key, 则返回指定的默认值

#12
# s = set([1, 2, 3])
# s.add(4)
# s.add((4, 5)) # set 只可以添加不可变的值
# s.add((4, 5)) # 不会重复添加
# s.add((4, 5, 6))
# s.remove(1)
# s.remove((4, 5, 6))
# x = "ABC" # {2, 3, 4, 'ABC', (4, 5)}
# s.add(x)
# x = "XYZ" # {2, 3, 4, 'ABC', (4, 5)}
# # s.remove(5) # KeyError: 5
# print(s)
# -------------------------------------------------------
# for x in s:
# 	print(x)
# 	if isinstance(x, tuple):
# 		for t in x:
# 			print(t)




# #from func import cipher
# #from func import *
# import math
# def cipher(a, b, c):
# 	if not isinstance(a,(int, float)):
# 		raise TypeError("a is not number!")
# 	elif a == 0:
# person("Jack", 24, job = "Engineer")
# person("Jack", 24, job = "Engineer")
# 		raise TypeError("a is zero")
# 	if not isinstance(b,(int, float)):
# 		raise TypeError("b is not number!")
# 	if not isinstance(c,(int, float)):
# 		raise TypeError("c is not number!")
# 	flag = b * b - 4 * a * c
# 	if flag < 0:
# 		return None
# 	elif flag == 0: 
# 		return -b / (2 * a)
# 	else:
# 		number1 = (-b + math.sqrt(flag)) / (2 * a)
# 		number2 = (-b - math.sqrt(flag)) / (2 * a)
# 		return (number1, number2)
# try:
# 	print(cipher(2, 3, 1))
# except Exception as e:
# 	print(e)
# -------------------------------------------------------
# def power(x, n = 2):
# 	s = 1
# 	while n > 0:
# 		n -= 1
# 		s = s * x
# 	return s
# print(power(2, 3))
# -------------------------------------------------------
# def enroll(name, gender, age = 17, city = "Beijing"):
# 	# age 默认为 17, city 默认为 Beijing
# 	print("name:", name)
# 	print("gender:", gender)
# 	print("age:", age)
# 	print("city:", city)
# enroll("Tom", "T", 18)
# enroll("Tom", "T", city = "Shanghai")
# enroll("Tom", "T", 1, "Shanghai")
# enroll("Tom", "T", cityz = "Shanghai") # Error enroll() got an unexpected keyword argument 'cityz'
# -------------------------------------------------------
# def add_end(list = None) :
# 	if list is None :
# 		list = []
# 	list.append("End")
# 	return list
# list = ["A", "B"]
# add_end(list)
# list = add_end()
# print(list)
# -------------------------------------------------------
# def calc(numbers) :
# 	sum = 0;
# 	for n in numbers:
# 		sum = sum + power(n)
# 	return sum
# def calc1(*numbers) :
# 	sum = 0;
# 	for n in numbers:
# 		print(n)
# 		sum = sum + power(n)
# 	return sum
# print(calc([1, 2, 3])) # 14
# print(calc(1, 2, 3)) # TypeError: calc() takes 1 positional argument but 3 were given
# print(calc1(1, 2, 3))
# print(calc1([1, 2, 3])) # 以*numbers定义型参类型会是 tuple, 数据实际接到数据是 ([1, 2, 3], ). TypeError: can't multiply sequence by non-int of type 'list'
# nums = set([1, 2, 3])
# print(type(nums))
# print(nums)
# print(calc1(*nums)) # *nums表示把nums这个list的所有元素作为可变参数传进去。
# -------------------------------------------------------
# def person(name, age, **kw) :  # ** => dict
# 	print("kw tyep is", type(kw))
# 	if "city" in kw : 
# 		print("city :", kw["city"])
# 	if "job" in kw:
# 		print("job :", kw.get("job"))
# 	print("name:", name, ", age:", age, ", other:", kw)
# person("Jion", 18, city = "Beijing")
# person(name = "Tom", city = "Beijing", age = 17)
# person("Jion", city = "Beijing", age = 18)
# extra = {'city': 'Beijing', 'job': 'Engineer'}
# person("Jion", 38, **extra)

# def person(name, age, *, city = "Beijing", job):
# 	# 要限制关键字参数的名字, 就要用到 "命名关键字参数"
# 	# * 后的参数, 被视为"命名关键字参数"
# 	print(name, age, city, job)
# person("Jack", 24, job = "Engineer")
# x = {"city":"Shanghai", "job":"Engineer"}
# person("Jack", 23, **x)
# person("Jack", 23, city = "Beijing", job = "Engineer")

# def person(name, age, *args, city, job):
# 	print(name, age, args, city, job)
# x = {"A":1, "B":2, "C":3}
# person("Jack", 23, x, city = "Beijing", job = "Engineer")
## 当实参为 *x 时, 会将实参中的key以tuple(元组)的形式, 传递到方法内
## 当实参为 x 时, 会将实参的整体内容做为tuple(元组)的一个元素, 传递到方法内
## 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数

# def product(x, y = 1, *args):
# 	result = x * y
# 	for i in range(0,len(args)):
# 		result = result * args[i]
# 	return result

# def product(x, *y):
# 	if len(y) == 0:
# 		return x
# 	res = x
# 	for i in y:
# 		res = res * i
# 	return res

# 测试
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
# 	print('测试失败!')
# elif product(5, 6) != 30:
# 	print('测试失败!')
# elif product(5, 6, 7) != 210:
# 	print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
# 	print('测试失败!')
# else:
# 	try:
# 		product()
# 		print('测试失败!')
# 	except TypeError:
# 		print('测试成功!')

# def recursive(x):
# 	if (x > 1):
# 		return x * recursive(x - 1)
# 	else:
# 		return 1

# print(recursive(998))


# 利用递归函数移动汉诺塔:
# def move(n, a, b, c):
# 	if n == 1:
# 		print('move', a, '-->', c)
# 	else:
# 		move(n-1, a, c, b)
# 		move(1, a, b, c)
# 		move(n-1, b, a, c)

# move(3, 'A', 'B', 'C')

# 切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print(L)
# print(L[1:4])
# L = list(range(100))
# arr = L[:];
# print(arr[:-1])

# def trim(s):
# 	if (s == ''):
# 		return ''
# 	if (ord(s[:1]) == 32):
# 		return trim(s[1:])
# 	elif (ord(s[-1:]) == 32):
# 		return trim(s[:-1])
# 	else:
# 		return s

# # 测试:
# if trim('hello  ') != 'hello':
# 	print('测试失败!')
# elif trim('  hello') != 'hello':
# 	print('测试失败!')
# elif trim('  hello  ') != 'hello':
# 	print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
# 	print('测试失败!')
# elif trim('') != '':
# 	print('测试失败!')
# elif trim('   ') != '':
# 	print('测试失败!')
# else:
# 	print('测试成功!')

# d = {"A":"1", "B":"2", "C":"3"}
# for k, v in d.items():
# 	print("key : {0}, value : {1}".format(k, v))
# for k in d:
# 	print("key :", k)
# for v in d.values():
# 	print("value :", v)

from collections import Iterable
# 判断一个对象是可迭代对象
# print(isinstance('abc', Iterable))

# def findMinAndMax(L):
# 	max = None
# 	min = None
# 	if (not isinstance(L, Iterable) or len(L) < 1):
# 		return min, max
# 	min = L[0]
# 	max = L[0]
# 	for x in L:
# 		if x > max:
# 			max = x
# 		elif x < min:
# 			min = x
# 	return min, max
# # 测试
# if findMinAndMax([]) != (None, None):
# 	print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
# 	print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
# 	print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
# 	print('测试失败!')
# else:
# 	print('测试成功!')

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
# print(L2)

# L = [x for x in range(100000000)]
# print(type(L))
# g = (x for x in range(10))
# print(type(g))
# while (True):
# 	try:
# 		print(next(g))
# 	except Exception as e:
# 		break
# for x in g:
# 	print(x)

# def fib(max):
# 	n, a, b = 0, 0, 1
# 	while n < max:
# 		yield(b)
# 		a, b = b, a + b
# 		n += 1
# 	return "done"

# f = fib(6)
# print(f)
# while (True):
# 	try:
# 		print(next(f))
# 	except Exception as e:
# 		print("end...", e.value)
# 		break

# for x in g:
# 	print(x)

# def odd():
# 	print("step 1")
# 	yield(1)
# 	print("step 2")
# 	yield(3)
# 	print("step 3")
# 	yield(5)
# o = odd()
# for x in o:
# 	print(x)

# 我写的:
# def triangles():
# 	old_list = []
# 	new_list = []
# 	i = 1
# 	while True:
# 		for j in range(i):
# 			le, re = 0, 0
# 			if(j - 1 < 0):
# 				le = 0 
# 			else: 
# 				le = old_list[j - 1]
# 			if(j >= len(old_list)):
# 				re = 0
# 			else:
# 				re = old_list[j]
# 			if (le == 0 and re == 0):
# 				new_list.append(1)
# 			else:
# 				new_list.append(le + re)
# 		yield(new_list)
# 		old_list = new_list
# 		new_list = []	
# 		i += 1
# 	return "done"

# 大神写的: 
# def triangles():
# 	t = [1]
# 	while True:
# 		yield t
# 		t= [t[i] + t[i-1] for i in range(1,len(t))]
# 		t.insert(0,1) # 第一位始终为 1
# 		t.append(1) # 最后一位始终为 1

# # 期待输出:
# # [1]
# # [1, 1]
# # [1, 2, 1]
# # [1, 3, 3, 1]
# # [1, 4, 6, 4, 1]
# # [1, 5, 10, 10, 5, 1]
# # [1, 6, 15, 20, 15, 6, 1]
# # [1, 7, 21, 35, 35, 21, 7, 1]
# # [1, 8, 28, 56, 70, 56, 28, 8, 1]
# # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
# 	print(t)
# 	results.append(t)
# 	n = n + 1
# 	if n == 10:
# 		break
# if results == [
# 	[1],
# 	[1, 1],
# 	[1, 2, 1],
# 	[1, 3, 3, 1],
# 	[1, 4, 6, 4, 1],
# 	[1, 5, 10, 10, 5, 1],
# 	[1, 6, 15, 20, 15, 6, 1],
# 	[1, 7, 21, 35, 35, 21, 7, 1],
# 	[1, 8, 28, 56, 70, 56, 28, 8, 1],
# 	[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
# 	print('测试通过!')
# else:
# 	print('测试失败!')
# name = "Jack"
# it = iter(name)
# print(next(it))
# for s in name:
# 	print(s.lower())

# def power(x, y):
# 	return x * y
# f = power
# def add(f, k_1, k_2 = 2, *num, **kwargs):
# 	s = 0
# 	print("k_1 power = {0}, {1}".format(k_1, k_2))
# 	for k in num:
# 		s += f(k, 3)
# 	for k, v in kwargs.items():
# 		print("key = {0}, value = {1}".format(k, v))
# 	print("s =", s)
# 	return s
# ss = list(range(10, 100, 10))
# dict = {"one":1, "two":2, "three":3, "four":4}
# print(add(f, 2, 5,*ss, **dict))

# def f(x):
# 	return x * x
# m = map(f, list(range(1, 10)))
# print(m)
# for k in m:
# 	print(k)

from functools import reduce

# def add(x, y):
# 	return x + y
# r = reduce(add, list(range(1, 4)))
# print(r)

def fn(x, y):
	return x * 10 + y
# print(reduce(fn, list(range(1, 10, 2))))

# def char2num(s):
# 	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 	return digits[s]

# print(reduce(fn, map(char2num, "1")))

# 所谓map, 就是遍历一个可迭代的对象, 把每个迭代的值, 带入到指定的fn中, 返回一个结果集的迭代器
# 所谓reduce, 就是将一个可迭代的对象, 第一次将迭代器中的前两个值, 带入指定的fn中, 接下来就会把fn返回的结果, 和迭代器的下一个值, 带入指定的fn中, 返回fn最后的计算结果
# print(reduce(fn, map(char2num, '13579')))

# def conversion(code):
# 	return chr(code)
#
# def join(before, after):
# 	return before + after
#
# print(reduce(join, map(conversion, range(65, 65 + 26))))

# def normalize(name):
# 	return name.lower().replace(name.lower()[0], name[0].upper(), 1)

# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)

# def prod(L):
# 	return reduce(lambda x, y : x * y, L)

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# 求素数(只能被 1 和 本身整除的数)
# def odd_item(): # 奇数生成器
# 	n = 1
# 	while(True):
# 		n += 2
# 		yield(n)

# def remove_card(n):
#  	return lambda x: x % n > 0 # 把 n 的倍数踢出去

# def get():
# 	yield(2)
# 	it = odd_item()
# 	while(True):
# 		n = next(it)
# 		it = filter(remove_card(n), it)
# 		yield(n)

# for i in get():
# 	if(i > 1000):
# 		break
# 	else:
# 		print(i)

# 方案A:
# def is_palindrome(n):
# 	s = str(n)
# 	l = len(s) // 2
# 	for i in range(l):
# 		if not s[i].__eq__(s[i - (2 * i + 1)]):
# 			return False
# 	return True

# def is_palindrome(n):
# 	s = str(n)
# 	l = len(s) // 2
# 	bef = s[:l]
# 	aft = s[l + len(s) % 2:]
# 	return bef.__eq__(aft[::-1])

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
# 	print('测试成功!')
# else:
# 	print('测试失败!')

# # 排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# def by_name(t):
# 	return t[0]
# def by_score(t):
# 	return t[1]

# L1 = sorted(L, key = by_name)
# print(L1)
# L2 = sorted(L, key=by_score, reverse = True)
# print(L2)

# def lazy_sum(*args):
# 	def sum():
# 		result = 0
# 		for x in args:
# 			result += x
# 		return result
# 	return sum

# s = lazy_sum(1, 2, 3, 4)
# print(s())


# def count():
# 	fs = []
# 	def f(i):
# 		def g():
# 			return i * i
# 		return g

# 	for i in range(1,4):
	
# 		fs.append(f(i))
# 	return fs

# f1, f2, f3 = count();

# print(f1())
# print(f2())
# print(f3())

# def createCounter():
# 	def items():
# 		n = 1
# 		while True:
# 			yield n
# 			n = n + 1
# 	it = items()
# 	def counter():
# 		return next(it)
# 	return counter

# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA())

# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# 匿名函数 Lambda
# def build(x, y):
# 	return lambda: x * x + y * y
# print(build(2, 3).__name__)

# def now():
# 	print("2018-01-09")

# f = now

# now()
# print(now.__name__)

# f()
# print(f.__name__)


# import time
# # 装饰器
# def timecost(func):
# 	def wrapper(*args, **kw):
# 		def fn(*args, **kw):
# 			start = int(time.time())
# 			print("Call {0}() Before [{1}]".format(func.__name__, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))))
# 			func(*args, **kw)
# 			print("Call {0}() After [{1}]".format(func.__name__, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time())))))
# 			end = int(time.time())
# 			print("Run Cost Time {0}s".format(end - start))

# 		return fn(*args, **kw)
# 	return wrapper

# @timecost
# def now_datetime(format):
# 	now = int(time.time())
# 	print(now)
# #调用 now_datetime 时, 相当于调用的是被 wrapper 加工过的新的方法
# now_datetime("%Y-%m-%d %H:%M:%S")
# print(now_datetime.__name__) # wrapper

# import functools
# def log(text):
# 	def decorator(func):
# 		@functools.wraps(func)
# 		def wrapper(*args, **kw):
# 			print(text, func.__name__)
# 			return func(*args, **kw)
# 		return wrapper
# 	return decorator

# @log("run")
# def test():
# 	print("hello decorator")

# test()
# print(test.__name__)

#偏函数
# print(int("101", 2)) # 5
# # 所谓偏函数，其实就是将一个已知参数和函数进行绑定，生成一个新的函数
# print(int("777", 8))

# from web.utils import reverse
# print(reverse("123"))

# import web.utils
# web.utils.welcome("Tom")

print("Hello World!")


