#Exercise 1
#finding the area of the triangle
def calculate_area(base,height):
    area=(1/2)*base*height
    return area

b=2
h=5
print(calculate_area(b,h))


#Exercise 2
'''def calculate_area(dimension1,dimension2,shape="triangle"):
    if shape=="triangle":
        area=1/2(dimension1*dimension2)
    elif shape=="rectangle":
        area=dimension1*dimension2
    else:
        print("Input shape is neither triangle nor rectangle")
        area=none
    return area '''   


    # Exercise 3 Print the pattern 

def print_pattern(n=100):
    for i in range(n):
        s=""
        for j in range(i+1):
            s+="*"
        print(s)    
     

print( print_pattern(100))     
