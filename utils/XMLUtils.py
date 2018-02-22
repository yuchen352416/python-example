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
		:param path: 文件的路径
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

	def get_node_by_key_value(self, nodes, kv_map):
		"""
		根据属性及属性值定位符合的节点，返回节点
		:param nodes: 所要查找的节点集合
		:param kv_map: 查找属性条件
		:return: 符合条件的节点集合
		"""
		result_nodes = []
		for node in nodes:
			if self.if_match(node, kv_map):
				result_nodes.append(node)
		return result_nodes

	def change_node_properties(self, nodes, kv_map, is_delete=False):
		"""
		修改/增加 /删除 节点的属性及属性值
		:param nodes: 需要操作属性的节点集合
		:param kv_map: 要新增, 修改或删除的属性map
		:param is_delete: 是否删除属性
		:return: True or False
		"""
		try:
			for node in nodes:
				for key in kv_map:
					if is_delete:
						if key in node.attrib:
							del node.attrib[key]
					else:
						node.set(key, kv_map.get(key))
			return True
		except Exception as e:
			print("操作节点属性失败...")
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def change_node_text(self, nodes, text, is_add=False, is_delete=False):
		"""
		改变/增加/删除一个节点的文本
		:param nodes: 节点集合
		:param text: 文本
		:param is_add: 是否新增
		:param is_delete: 是否删除
		:return: True or False
		"""
		try:
			for node in nodes:
				if is_add:
					node.text += text
				elif is_delete:
					node.text = ""
				else:
					node.text = text
			return True
		except Exception as e:
			print("操作节点文本失败...")
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def create_node(self, tag, property_map, content):
		"""
		新建节点
		:param tag: 节点名
		:param property_map: 节点属性
		:param content: 节点文本
		:return: 新节点
		"""
		element = et.Element(tag, property_map)
		element.text = content
		return element

	def add_child_node(self, node, element):
		"""
		给指定节点添加子节点
		:param node: 指定操作节点
		:param element:
		:return: True or False
		"""
		try:
			node.append(element)
			return True
		except Exception as e:
			print("添加新节点失败...")
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def del_node_by_tag_key_value(self, nodes, tag, kv_map):
		"""
		同过属性及属性值定位一个节点，并删除之
		:param nodes: 父节点列表
		:param tag: 子节点标签
		:param kv_map: 属性及属性值列表
		:return: True or False
		"""
		try:
			for parent in nodes:
				childs = parent.getchildren()
				for child in childs:
					if child.tag == tag and self.if_match(child, kv_map):
						parent.remove(child)
			return True
		except Exception as e:
			print("操作节点失败...")
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def list(self):
		"""
		返回xml文件中所有节点数组
		:return:
		"""
		result = []
		for node in self.tree.iter():
			# "Tag": node.tag
			# "Attributes": node.attrib
			# "Data":, node.text
			result.append(node)
		return result


path = "/Users/smile/test.xml"
xml = XMLUtils(path)
result = xml.read() # 读取
print(result)

## 遍历节点
# xml.list()
# 查询节点
# nodes = xml.find_nodes("country/neighbor")
# print(nodes)
# nodes = xml.get_node_by_key_value(xml.tree.iter(), {"direction": "W", "name": "Switzerland"})
# nodes = xml.get_node_by_key_value(xml.tree.iter(), {"direction": "W", "name": "Mr.Li"})
# print(nodes)
# xml.change_node_properties(nodes, {"directions": "F"}, is_delete=True)

# nodes = xml.find_nodes("country/year")
# xml.change_node_text(nodes, "年", is_add=True)

# nodes = xml.get_node_by_key_value(xml.tree.iter(), {"direction": "W", "name": "Mr.Li"})
# print(nodes)
# new_node = xml.create_node("xxx", {"x": "1", "xx": "2"}, "XXXX")
# xml.add_child_node(nodes[0], new_node)

nodes = xml.find_nodes("country/neighbor")
xml.del_node_by_tag_key_value(nodes, "xxx", {"x": "1", "xx": "2"})


result = xml.wite(path) # 写入
print(result)



