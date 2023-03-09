# Functions in Python

def find_total(exp):
    total=0
    for item in exp:
        total+=item
    return total

bharat_expenses=[20,30,45]
bharat_total=find_total(bharat_expenses)  

bilal_expenses=[45,67,34]
bilal_total=find_total(bilal_expenses)
print(bharat_total)
print(bilal_total)


#Function for finding the volume of the cylinder
def cylinder_volume(radius,height):
    volume=3.14*(radius**2)*height
    return volume

r=5
h=10
print(cylinder_volume(r,h))