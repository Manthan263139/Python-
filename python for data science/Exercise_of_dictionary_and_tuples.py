#Exercise 1
lists={'china':'143','india':'136','usa':'32','pakistan':'21'}
for population in lists:
    print(population,"==>",lists[population])
lists['russia']='156'
print(lists)

#Exercise 2
'''stocks={
    'info':[600,630,620],
    'ril':[1430,1490,1567],
    'mtl':[234,180,160]
}
 def print_all():
    for stoks,price_list in stocks.items():'''
        
#exercise 3
def circle_calc(radius):
    area=3.14*radius*radius
    circumference=2*3.14*radius
    diameter=2*radius
    return area,circumference,diameter


if __name__=="__main__":
    r=input("Enter the radius ")
    r=float(r)
    area,c,d=circle_calc(r)
    print(f"area{area},circumference{c},diameter{d}")  



