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
# semi=int(input("enter your semister:"))
# finall=int(input("enter your final marks:"))
# total=semi*0.4+finall*0.6
# if total>=90:
    # print("your grade is A")
# elif total>=80:
    # print("your grade is B")
# elif total>=70:
    # print("your grade is C")
# elif total>=60:
    # print("your grade is D")
# else:
    # print("your grade is F")
# print("your total marks is :", total)
# data_type=input("enter your data type:")
#int , float , str , list , tuple , dict , set
# when we crweate a new data type that uses the basic ones call it data structure
#list

my_list=[1,2,3,4,5]
# list2=["mohammad",20,5.6,True]
#firs operation  on list
# len_list=len(my_list)
#append is used to add an element at the end of the list
# my_list.append(6)
# print("my_list",my_list)
#extend is used to add multiple elements at the end of the list
# my_list.extend([7,8,9])
# print("my_list after extend",my_list)
#position based operations
#insert is used to add an element at a specific position
#index starts from 0

my_list.insert(0,0)
#pop is used to remove an element from a specific position
my_list.pop(3)
my_list.pop((my_list)-1)
#change an element at a specific position
my_list[2]="moe"
print("my_list after insert and pop",my_list)
#list are mutable : we can change them