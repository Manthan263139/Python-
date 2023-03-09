#list in python
mithai=['halva','kheer','jalebi','gulabjamun']
print(type(mithai))
print(mithai[0])
print(mithai[-1])

#slicing in the list
print(mithai[1:3])
print(mithai[:])
print(len(mithai))
print('halva'in mithai)

# Add another item in the list
mithai.append('laddu')
print(mithai)
mithai.insert(2,'laddu')

tikha=['samosa','sev']
food=mithai+tikha
print(food)

mithai[0:2]="samosa"
print(mithai)
mithai[0:6]=['samosa']
print(mithai)