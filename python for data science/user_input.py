# User input in python
n1=input("Enter first number")
n2=input("Enter second number")
print(n1,n2)
sum=float(n1)+float(n2)
print(sum)


#exercise for user input
n1=input("Enter the base of the triangle")
n2=input("Enter the height of the triangle")
area=(1/2)*float(n1)*float(n2)
print(area)

#Exercise 2
file_name=input("Enter the file name with extension:")
print("File name without extension:",file_name[:len(file_name)-4])