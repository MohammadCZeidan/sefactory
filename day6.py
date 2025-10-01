#last day was list 
#today we will learn about tuple
#data structures
#list\
my_list=[1,2,3,4,5]
#tuple
#what is the difference between list and tuple
#list are mutable : we can change them
#tuple are immutable : we can not change them
#tuple is python specific data structure
my_tuple=(1,2,3,4,5)
len_tuple=len(my_tuple)
print("my_tuple",my_tuple)
my_tuple.append(6) #does not work
my_tuple.extend([7,8,9]) #does not work
my_tuple.insert(0,0) #does not work
my_tuple.pop(3) #does not work
my_ruple[2]="moe" #does not work
#but we can access the elements of the tuple
print(my_tuple[2]) #works

