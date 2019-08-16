def describe_pet(animal_type, pet_name): #括号里面是两个形参
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry') #括号里面是两个实参，位置实参
describe_pet('dog', 'willie') #传递实参,按顺序显示


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
#这样的话顺序不一样，结果也是一样的了



def describe_pet(pet_name, animal_type='dog'):#有默认值的形参
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='whillie')
describe_pet('whillie') #未指定实参赋值给pet_name