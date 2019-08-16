import json

filename = 'numbers.json'
with open(filename) as file_object:
	numbers = json.load(file_object) 

print(numbers)

# json.load()加载numbers.json内容,将列表读取到内容中
