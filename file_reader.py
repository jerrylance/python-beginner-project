# 函数open(参数： 要打开的文件的名称)

# 关键词with 不需要访问文件后可以将其关闭

# 方法read() 读取文件全部内容

with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)
# rstrip()消除文件末尾空行
	print(contents.rstrip())

# 注意引用路径不要粘贴复制\和/的区别
file_path = 'D:/python学习/python程序/text_files/pi_digits.txt.'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())


file_path = 'D:/python学习/python程序/text_files/pi_digits.txt.'
with open(file_path) as file_object:
	for line in file_object:
		print(line.rstrip())

# 每行读取
file_path = 'D:/python学习/python程序/text_files/pi_digits.txt.'
with open(file_path) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())



file_path = 'D:/python学习/python程序/text_files/pi_digits.txt.'
with open(file_path) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


pi_string = ''
for line in lines:
	pi_string += line.strip()   #rstrip()和 strip()区别

print(pi_string)
print(len(pi_string))