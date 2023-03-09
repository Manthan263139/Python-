#Exception handling in python 

#Exception are errors detected at the time of program execution 
#print(1/0)
#print('abc'+2)

x=input("Enter the number1 :")
y=input("Enter the number2 :")
try:
    z=int(x)/int(y)
except Exception as e:
    print('exception occured:',e)
    z=None

print("division is: ",z)