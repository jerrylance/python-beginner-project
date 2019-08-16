filename = 'programming.txt'

# filename是要打开文件， w是写入模式会覆盖原文档, write()写入
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# a是附加模式，不修改之前内容，同样使用write(写入
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a brower.\n")

