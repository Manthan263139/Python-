#classes and objects in python 

class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o

    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
            
        elif self.occupation=="actor":
            print(self.occupation,"shoots a film")

            
    def speaks(self):
         print(self.name,"says how are you?")

   

tom=Human("Tom cruise","actor")
tom.do_work()
tom.speaks()            
