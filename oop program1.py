class Myclass:
    def __init__(self,x,y):
        self.name=x
        self.age=y
        self.courses=[]
    
    def __str__(self):
        msg=" "+self.name+" "+str(self.age)+" "+str(self.courses)
        return msg
    
    def add_course(self,cour):
        self.courses.append(cour)

obj1=Myclass("vishal",21)
print str(obj1)
obj1.add_course("CSE")
print str(obj1)