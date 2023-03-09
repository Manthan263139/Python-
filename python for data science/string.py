# string in python
food='samosa'
print(food[1])

# slicing in the string 
print(food[0:2])

# finding the length of the string
print(len(food))

# finding the string is  present or not 
myfood='samosa,jalebi'
print('jalebi'in myfood)
print('biriyani'not in myfood)

# replacing one string to another 
print(myfood.replace('samosa','biryani'))

# print all the function related to the string 
print(dir(myfood))

# converting the string into lower case and uppercase
print(myfood.upper())
s='78'
print(s.isdigit())
s2='67 chor manthan joshi'
print(s2.isdigit())

print(myfood.index('jalebi'))

# concatinate a number and a text 
states=29
text='states in india'
#print(text+states) # wrong approach show error

print(text+str(states))

# use tripal cot for multi line string 
poem='''hello my name is manthan joshi
'''
print(poem)

# using tab in the string
s3='hey\bro'
print(s3)




