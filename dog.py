# self在调用类中必须要有，记住def __init__(self, _, _):
# self并不是关键词，可以用a，b之类的取代，但是为了规范代码一般用self
class Dog():

	def __init__(self, name, age): # 初始化注意双下划线
		# 获取储存在形参name中的值，并将其储存到变量name中
		self.name = name    # self指的是类实例对象本身,不是类本身
		self.age = age
	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over!")

# 实例
my_dog = Dog('willie', 6)
your_dog =Dog('lucy', 3)

#访问属性
print("My dog''s name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.\n")

#调用方法
my_dog.sit()

print("\nMy dog's name is " + your_dog.name.title() + ".")
print("My dog is " + str(your_dog.age) + " years old.")
your_dog.sit