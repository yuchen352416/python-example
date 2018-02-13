#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
import happybase as hb


class HBaseDao:

	def __convert(self, dict):
		result = {}
		for k, v in dict.items():
			result[k.decode("utf-8")] = v.decode("utf-8")
		return result

	def __init__(self, table, host="localhost", port=9090):
		"""
		:param table: table name
		:param host: h-base host
		:param port: h-base port
		"""
		try:
			self.__connection = hb.Connection(host, port)
			self.__connection.open()
			self.__table = self.__connection.table(table)
		except Exception as e:
			print("连接 HBase {0}:{1} 失败...".format(host, port))
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)

	def insert(self, rowkey, columns):
		# 将字符编码成2进制
		"""
		:param rowkey: row key
		:param columns: {"column_family:column_qualifier":"value"}
		:return: True or False
		"""
		try:
			rowkey = rowkey.encode(encoding='utf-8')
			columnsByte = {}
			for k, v in columns.items():
				columnsByte[k.encode(encoding='utf-8')] = v.encode(encoding='utf-8')
			self.__table.put(rowkey, columnsByte) # 插入数据
			return True
		except Exception as e:
			print("插入 HBase 失败, row_key:{0}, data:{1}".format(rowkey, columns))
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def insert_all(self, data):
		"""
		:param data: {"row_key":{"column_family:column_qualifier":"value"}}
		:return: True or False
		"""
		try:
			# 使用batch一次插入多行数据
			bat = self.__table.batch()
			for row_key, columns in data.items():
				columnsByte = {}
				for k, v in columns.items():
					columnsByte[k.encode(encoding='utf-8')] = v.encode(encoding='utf-8')
				bat.put(row_key.encode(encoding='utf-8'), columnsByte)
			bat.send()
			return True
		except Exception as e:
			print("插入 HBase 失败 data:{0}".format(data))
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def delete_row(self, row_key):
		try:
			bat = self.__table.batch()
			bat.delete(row_key)
			bat.send()
			return True
		except Exception as e:
			print("删除 HBase 失败 row_key:{0}".format(row_key))
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def delete_columns(self, row_key, *columns):
		try:
			if len(columns) == 0:
				raise AttributeError("缺失要删除的列")
			self.__table.delete(row_key, columns)
			return True
		except Exception as e:
			print("删除 HBase 失败 row_key:{0}".format(row_key))
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
		return False

	def query(self, *row_keys):
		'''
		:param row_keys:
		:return: {"row_key":{"column_family:column_qualifier":"value"}}
		'''
		result = None
		if len(row_keys) == 1:
			result = self.__table.row(row_keys[0])
			result = self.__convert(result)
			result = {row_keys[0]:result}
		elif len(row_keys) > 1:
			result = {}
			items = self.__table.rows(row_keys)
			for item in items:
				result[item[0].decode("utf-8")] = self.__convert(item[1])
		return result

	def query_all(self):
		items =  self.__table.scan()
		result = {}
		for k, v in items:
			result[k.decode("utf-8")] = self.__convert(v)
		return result




# -----------------------------------------------------------------------------

dao = HBaseDao("SCORE")
# result = dao.insert("row_key_5", {"F:1": "李", "F:2": "述", "F:3": "昱"})
# result = dao.insert("row_key_5", {"F:1": "A", "F:2": "B", "F:3": "C"})
# result = dao.insert_all({"row_key_6":{"F:1":"Z", "F:2":"Y", "F:3":"X"}, "row_key_7":{"F:1":"Q", "F:2":"W", "F:3":"E", "F:4":"R"} })
# result = dao.delete_row("row_key_5")
result = dao.delete_columns("row_key_4", "M:1")
# result = dao.query("row_key_5")
# result = dao.query("row_key_5", "row_key_6", "row_key_7")
# result = dao.query_all()
print(result)
