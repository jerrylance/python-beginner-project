# 表示汽车的类
class Car():

	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

my_new_Car = Car('audi', 'a4', 2016)
print(my_new_Car.make)
print(my_new_Car.get_descriptive_name())

