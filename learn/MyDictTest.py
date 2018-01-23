#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging, unittest
from learn.MyDict import MyDict


class TestMyDict(unittest.TestCase):

	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')

	def test_init(self):
		d = MyDict(a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = MyDict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = MyDict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

	def test_keyerror(self):
		d = MyDict()
		with self.assertRaises(KeyError): # 判断抛出的异常是 KeyError
			value = d['empty']

	def test_attrerror(self):
		d = MyDict()
		with self.assertRaises(AttributeError): # 测试未通过, 因为这里抛出的是KeyError
			value = d.empty

