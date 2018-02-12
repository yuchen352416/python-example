#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import traceback
from functools import reduce


class BaseDao:
	def __exec(self, sql):
		flag = False
		# 使用cursor()方法获取操作游标
		cursor = self.db_connect.cursor()
		try:
			# 执行sql语句
			cursor.execute(sql)
			# 提交
			self.db_connect.commit()
			flag = True
		except Exception as e:
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
			# 如果发生错误则回滚
			self.db_connect.rollback()
		# 关闭数据库连接
		self.db_connect.close()
		return flag

	def __init__(self, user, passwd, host, db, port=3306):
		# 打开数据库连接
		self.db_connect = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset="utf8")

	def insert(self, table, **kw):
		'''
		:param table: tablename
		:param kw: {"insert_field":"insert_value"}
		:return: True or False
		'''

		# SQL 插入语句
		fieds = reduce(lambda x, y: "{0}, {1}".format(x, y), kw.keys())
		values = reduce(lambda x, y: "{0}, {1}".format("\"%s\"" % x if type(x) == str else x, "\"%s\"" % y if type(y) == str else y), kw.values())
		sql = "INSERT INTO {0} ({1}) VALUES({2})".format(table, fieds, values)
		return self.__exec(sql)

	def delete(self, table, id):
		'''
		:param table: tablename
		:param id: Primary Key
		:return: True or False
		'''

		sql = "DELETE FROM {0} WHERE ID = {1}".format(table, id)
		return self.__exec(sql)

	def update(self, table, id, **kw):
		'''
		:param table: tablename
		:param id: Primary Key
		:param kw: {"update_fields": "update_value"}
		:return:
		'''

		# 拼装 SQL
		fields = ""
		for k, v in kw.items():
			fields += k
			fields += "="
			fields += "\"%s\"" % v if type(v) == str else str(v)
			fields += ","
		fields = fields[:-1]
		sql = "UPDATE {0} SET {1} WHERE id = {2}".format(table, fields, id)
		return self.__exec(sql)

	def query(self, table, **kw):
		"""
		:param table: table_name
		:param kw: query_condition
		:return: [{}, {}]
		"""

		# 拼装 SQL
		condition = ""
		if kw:
			condition = "WHERE "
		for k, v in kw.items():
			condition += k
			condition += "="
			condition += "\"%s\"" % v if type(v) == str else str(v)
			condition += " AND "

		condition = condition[:-5]
		sql = "SELECT * FROM {0} {1}".format(table, condition)
		# 使用cursor()方法获取操作游标
		# pymysql.cursors.DictCursor 设置查询结果为 dict类型
		cursor = self.db_connect.cursor(pymysql.cursors.DictCursor)
		try:
			# 执行SQL语句
			cursor.execute(sql)
			# 获取所有记录列表
			rows = cursor.fetchall()
			return rows
		except Exception as e:
			# 打印错误的堆栈信息
			info = traceback.format_exc()
			print(info)
			# 如果发生错误则回滚
			self.db_connect.rollback()
		# 关闭数据库连接
		self.db_connect.close()


dao = BaseDao("root", "root", "127.0.0.1", "Test")
# result = dao.insert("USER", id="2", name="Jack", age=17, city="Shanghai")
# print(result)
# result = dao.delete("USER", 2)
# print(result)
# result = dao.update("USER", 1, name="小红", age=23, city="Shanghai")
# print(result)

result = dao.query("USER")
print(result)

