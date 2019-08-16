import json

# 创建数字列表
numbers = [2, 3, 5, 7, 11, 13]

# 指定将数字列表储存到其中的文件的名称
filename = 'numbers.json'
with open(filename, 'w') as file_object:
	json.dump(numbers, file_object)

# 函数json.dump() 第一个实参为要储存的数据numbers，第二个实参为可用于储存数据的文件对象