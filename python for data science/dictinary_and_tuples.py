#dictionary and tuples in the python 

#dictionary in python
captains={'india':'virat','pakistan':'sarfaraz','sri lanka':'dimuth'}
print(captains)
print(captains['india'])
print(captains.keys())
print(captains.values())
captains['england']='joe root'
print(captains)

for team in captains:
    print(team,"-->",captains[team])

print('australia' in captains)
print(captains.get('india'))

# Tuples in python 
# tuples is same as list in python but a little diffrence
point=(4,10)
print(type(point))