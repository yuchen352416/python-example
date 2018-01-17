
# 类里的方法, 都要有接收实例的一个变量, 我的理解是将传入实例, 执行某些行为.

class Animal(object):
	def __init__(self, args):
		super(Animal, self).__init__()
		self.__name = args.get("name")
		self.age = args.get("age")

	def call(self):
		print("Animal(name:{0}, age:{1}) Call....".format(self.__name, self.age));

	def setAnimalInfo(self, *, name, age):
		self.__name = name
		self.age = age

cat = Animal({});
cat.setAnimalInfo(name = "tom", age = 2)
cat.call()
cat.age = 3
print(cat.age)
print(cat._Animal__name) # 不建议这样访问
# cat.__name = "jack"
# print(cat.__name)
cat.call()

# Python 可以在类的方法内用 self 绑定属性, 也可在类的外部绑定属性
