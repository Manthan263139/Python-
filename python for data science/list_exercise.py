#list exercise in the python

#exercise 1
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)

heros.insert(3,'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)


# Exercise 2
exp=[2200,2350,2600,2130,2190]
print("doller that expend extra in feb as compare to the january",exp[1]-exp[0])
print("sum of first third year",exp[0]+exp[1]+exp[2])
print("sum of all the expenses ",exp[0]+exp[1]+exp[2]+exp[3]+exp[4])
