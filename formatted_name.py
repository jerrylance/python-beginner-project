def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()#结果返回到函数调用行

musician = get_formatted_name('jimi', 'hendrix')#按顺序指定first和lastname，就是位置实参
print(musician)#return 后面的表达式的值，就是函数调用的值


def get_formatted_name(first_name, middle_name, last_name):
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)