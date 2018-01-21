#!/usr/bin/env python
# -*- coding: utf-8 -*


class Book(object):
	def __init__(self, name):
		# super(Book, self).__init__()
		self.name = name

	def getName(self):
		return self.name


class Literature(object):

	def __init__(self, author):
		# super(Literature, self).__init__()
		self.author = author

	def getAuthor(self):
		return self.author


class Biography(object):
	def __init__(self, heroName):
		super(Biography, self).__init__()
		self.heroName = heroName

	def getHeroName(self):
		return self.heroName


class Youth(Book, Literature, Biography):
	def __init__(self, name, author, heroName):
		Book.__init__(self, name)
		Literature.__init__(self, author)
		Biography.__init__(self, heroName)

	def getInfo(self):
		return "书名: {0}, 作者: {1}, 主人公: {2}".format(
			self.getName(), self.getAuthor(), self.getHeroName())


book = Youth("青春", "J.M.库切", "约翰")
print(book.getName())
print(book.getAuthor())
print(book.getHeroName())
print(book.getInfo())
