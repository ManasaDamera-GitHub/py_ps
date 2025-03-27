class Human:
    def __init__(self,name1,age1):
        self.name=name1
        self.age=age1
        print("human object created")
class Student:
    def __init__(self,name1,age1):
        super().__init(name1,age1)
        print("student obj created")

std1=Student('manasa',25)
print(std1.name)
        