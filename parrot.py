#input 函数可以使程序暂停并等待用户输入，在cmd下运行可以看出

message = input("Tell me something, and I will repeat it back to you : ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")


# 输入quit，不打印quit

prompt = "\nTell me something, and I will repeat it back to you : "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit' :
	message = input(prompt)
	
	if message != 'quit' :
		print(message)

# True, false函数
prompt = "\nTell me something, and I will repeat it back to you : "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False 
	else:
		print(message)
