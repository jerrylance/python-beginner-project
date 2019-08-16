class Car(): #类的继承

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def updated_odometer(self, mileage):
		"""
		将里程表读数设置为指定的值
		禁止将里程表读数往回调
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		"""将里程表读数增加指定的量, +=运算符"""
		self.odometer_reading += miles

# 子类 （父类or超类）
# super() 将父类和子类关联起来，让ElectricCar包含Car里面的所有属性
# 如下三行代码实现继承

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())