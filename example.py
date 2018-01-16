class Student(object):
	"""docstring for Student"""
	def __init__(self, kw):
		super(Student, self).__init__()
		self.kw = kw
		
	def getValue(self):
		return self.kw
	def setValue(self, **kw):
		self.kw = kw



x = {"a":1, "b":2}
s = Student(x)

print(s.getValue())