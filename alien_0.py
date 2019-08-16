alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)


#创建一个用来储存外星人的空列表
aliens = []

#创建30个绿色的外星人,用函数range()
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
	print(alien_number)	
#显示前五个外星人
for alien in aliens[:5]:
	print(alien)
print("...")

#显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

aliens = []
for alien_number in range(0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
	
	
for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
		
for alien in aliens[:5]:
	print(alien)
print("...")
