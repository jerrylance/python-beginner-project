#如果try无异常，则跳过except代码块，如果try异常，会去匹配except代码块


try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")


print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirtst number: ")
	if first_number == 'q':
		break
	second_number = input("Second_number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't divede by 0")
	else:
		print(answer)
