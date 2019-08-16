prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)"
# While True: 开头的循环将不断运行
while True:
	city = input(prompt)

	if city == 'quit':
		break         # break 打断循环
	else:
		print("I'd love to go to " + city.title() + "!")
		