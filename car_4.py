class Car():

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
		"""将里程表读数设置为指定的值"""
		self.odometer_reading = mileage

my_new_Car = Car('audi', 'a4', 2016)
print(my_new_Car.get_descriptive_name())

# 通过方法修改属性的值
my_new_Car.updated_odometer(24)
my_new_Car.read_odometer()