def make_pizza(*toppings):   # 加了*号是空元组，不可变
	"""打印顾客点的所有配料"""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):   # 加了*号是空元组，不可变
	"""概述要制作的比萨"""
	print("\nMaking a pizza with the following toppings:")
	for  topping in toppings:
		print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 想要让函数接受不同类型的实参，在函数定义时把接纳任意数量实参的形参放最后
def make_pizza(size, *toppings):
	"""概述要制作的比萨"""
	print("\nMaking a " + str(size) + 
		"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

