#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import traceback
import happybase as hb


class HBaseDao:

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
		:return:
		"""
		rowkey = rowkey.encode(encoding='utf-8')
		columnsByte = {}
		for k, v in columns.items():
			columnsByte[k.encode(encoding='utf-8')] = v.encode(encoding='utf-8')
		self.__table.put(rowkey, columnsByte)


dao = HBaseDao("SCORE")
dao.insert("row_key_5", {"F:1": "ABC", "F:2": "DEF", "F:3": "JHI"})
