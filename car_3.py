class Car():

	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		"""打印一条指出汽车里程的消息"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_Car = Car('audi', 'a4', 2016)
print(my_new_Car.get_descriptive_name())

# 通过实例直接修改属性的值
my_new_Car.odometer_reading = 23
my_new_Car.read_odometer()