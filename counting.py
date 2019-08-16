# while循环搭配+=用法
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2  == 0:
		continue  #忽略后续代码，返回循环开头，满足条件继续循环，不执行print

	print(current_number)

x = 1
while x <= 5:
	print(x) 
	x += 1


#下面这个例子会变成无限循环
x = 1
while x <= 5:
	print(x)
#break 