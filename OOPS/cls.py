# class, obj, self , instance and static variables
# 
# 
# 
# class definition 
# class Calculator:
#     def sum(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b

# object
# cal1=Calculator()
# print(cal1.sum(2,5))


# construcors

class Human:
    # static variable
    species_name="Homosep"
    def __init__(self,name1,age1,dob1):
        #instance variables
        self.name=name1 
        self.age=age1
        self.dob=dob1
    def self_intro(self):
        print(self.name)
    

human1=Human("menny",10,"25/2/2015")
human2=Human("kenny",7,"22/6/2015")


print(human1.name)
print(human1.age)
print(human1.dob)
print(human2.name,"age:",human2.age,human2.dob)
