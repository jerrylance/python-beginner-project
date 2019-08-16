def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

# 这是一个无限循环！
"""
while True:
	print("\nPlease tell me your name:")
	f_name =input("First_name: ")
	l_name =input("Las name: ")

	get_formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + get_formatted_name + "!")
"""
# 没有定义退出条件

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if f_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

	