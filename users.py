user_0 = {
	'username' : 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

for key, value in user_0.items():
	print("\nKey: " + key)
	print("value: " + value)

#key, value can be k, v, the solution is the same

users = {
	'aeinstein': {'first': 'albert',
				  'last': 'einstein',
				  'location': 'princeton'},
	'mcurie':{'first': 'marie',
	          'last': 'cutie',
	          'location': 'paris'},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
