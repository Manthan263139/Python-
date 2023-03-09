#Exercise 1
class Employee:
    def __init__(self,i,n):
        self.id=i
        self.name=n

    def display(self):
        print(f"Id: {self.id} \nName:{self.name}")

       

manthan=Employee("123","manthan joshi")
manthan.display()
