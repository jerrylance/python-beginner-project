def build_profile(first, last, **user_info): #两个*号空字典
	"""创建一个字典，其中包含我们知道的有关用户的一些"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)