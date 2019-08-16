#for 循环不要忘记冒号,每个缩进的代码行都是循环的一部分
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
		
	
magicians = ['alice', 'david', 'carolina']
for magician in magicians:	
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Thank you, everyone. That was a great magic show!")

print("\n")
for value in range(1,5):  #输出不包含第二个也就是末尾的值，这个很坑啊
	print(value)
