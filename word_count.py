def count_words(filename):
	"""计算一个文件大致包含多少单词"""
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + "does not exist."
		print(msg)
	else:
		#计算文件大致包含多少单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','siddhartha.txt','moby_dict.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

# 第二个txt不存在，但是也打印出来了
# 如果加入了pass则会跳过不存在文件
"""
except FileNotFoundError:
	pass

"""
print('\n')
def count_words(filename):
	"""计算一个文件大致包含多少单词"""
	try:
		with open(filename, encoding='utf-8') as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		#计算文件大致包含多少单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt','siddhartha.txt','moby_dict.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

	