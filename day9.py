#oop
#object oriented programing
#list is a complex data type=> we call it data strcuture 


#car
#color:blue
#brand :toyota
#engine:hybrid
#windows:Tinted


# name ="joe"
# grade ="10"
# names =["joe","moe"]
# grades =["10",20]



#create a class to group multipe attribute for a single variable
####class =classname
### attributes and method
#the self key word represent the instance create then (not the class)defined the class
class Student:#class StudentGrade
    def __init__(self,name,grade):#self here is important
        # print("om init")
     self.name=""
     self.grade=0

    def intro_yourself(self):
      print("hello, im ", self.name, "i got ", self.grade)
     
    def checked_if_passed(self):
       if self.grade>=50:
        print(self.name,"has passed")
       else:
           print(self.name,"has not passed")
  
#create an instance of the class
s1= Student("joe",10)
s2= Student("moe",20)

print("s1")
print(s1.name)
print(s1.grade)
s1= Student("joe",10)
s2= Student("moe",20)
s1.intro_yourself()
s2.intro_yourself()

# for s in Student:
#  s.checked_if_passed()
