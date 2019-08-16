cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #永久按照字母顺序排列
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #传递函数按字母相反顺序排列
print(cars) 

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse() #永久按反转顺序排列
print(cars)