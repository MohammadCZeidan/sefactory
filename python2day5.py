#flow control 
#if i want my program to make decisions 
# name=input("enter your name:")
# age=int(input("enter your age:"))
# if name== "mohammad" and age==20:
    # print("welcome mohammd")
# elif name=="ali":
    # print("welcome ali")
# else:
    # print("welcome :", name)
    # print("your age is :", age)
semi=int(input("enter your semister:"))
finall=int(input("enter your final marks:"))
total=semi*0.4+finall*0.6
if total>=90:
    print("your grade is A")
elif total>=80:
    print("your grade is B")
elif total>=70:
    print("your grade is C")
elif total>=60:
    print("your grade is D")
else:
    print("your grade is F")
print("your total marks is :", total)