players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  #切片索引
print(players[:4])
print(players[2:])
print(players[-3:])

print("\n")
print("Here are the first three players on my team")
for player in players[:3]:
	print(player.title())

