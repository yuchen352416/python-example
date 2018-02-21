#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
from xml.etree import ElementTree as et


class XMLUtils(object):
	def __init__(self, file_path):
		self.__path = file_path
		self.tree = None

	def read(self):
		'''
		读取并解析xml文件
		return: True or False
		'''
		try:
			tree = et.ElementTree()
			tree.parse(self.__path)
			self.tree = tree
			return True
		except Exception as e:
			print("读取XML失败...")
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def wite(self, path):
		"""
		写入XML到文件
		:param path:
		:return: True or False
		"""
		try:
			self.tree.write(path, encoding="utf-8", xml_declaration=True)
			return True
		except Exception as e:
			print("写入XML失败...")
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def if_match(self, node, kv_map):
		"""
		判断某个节点是否包含所有传入参数属性
		:param node: 节点
		:param kv_map: 属性及属性值组成的map
		:return: True or False
		"""
		for key in kv_map:
			if node.get(key) != kv_map.get(key):
				return False
		return True

	def find_nodes(self, path):
		"""
		查找某个路径匹配的所有节点(注意: 路径中不能有<根节点>)
		:param path: 路径
		:return: 匹配的所有节点
		"""
		try:
			return self.tree.findall(path)
		except Exception as e:
			print("写入XML失败...")
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return None

	def get_node_by_key_value(self, nodelist, kv_map):
		pass




	def list(self):
		for node in self.tree.iter():
			print("Tag =", node.tag, ", Attribute =", node.attrib, ", Data =", node.text)







path = "/Users/smile/test.xml"
xml = XMLUtils(path)
result = xml.read() # 读取
print(result)


# result = xml.wite(path) # 写入
# print(result)


## 遍历节点
# xml.list()

nodes = xml.find_nodes("country/neighbor")
print(nodes)
