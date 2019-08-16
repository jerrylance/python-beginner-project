#文件如果不存在演示（没有alice.txt文件）
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError: #代码块FileNotFoundError:
	msg = "Sorry, the file " + filename + "doen not exist."
	print(msg)


#下列语句要在python程序中运行
title = "Alice in Wonderland"
title.split()

#文件存在（有alice.txt文件）

filename = 'D:/python学习/python程序/text_files/alice.txt'

try:
	with open(filename, encoding = 'utf-8') as f_obj:
		contents = f_obj.read()
except FileNotFoundError as e: #代码块FileNotFoundError:
	msg = "Sorry, the file " + filename + "doen not exist."
	print(msg)
else:
	#计算文件大致包含多少个单词
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " world.")
