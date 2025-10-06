#function cotinue
#scope of variable
#global variable
# # x=10
# def fun():
    # global x
    # x=5
    # print(x)
# fun()
# print(x)    
# local variable
# def fun():
    # x=10
    # print(x)
# fun()
# print(x)
# excersise
# x=10
# def f1():
    # y=5
    # print(x)
    # def f2():
        # z=12
        # z= y+x
        # print(z)
# def f3():
#    t=15



#lambda function
#just a function that can be written in a single line
# def multi(x,y):
    # return x*y
# lambda x ,y:x*y
# print(multi(5,6))

# multi=lambda x ,y:x*y
# print(multi(5,6))


#write a function that changes from calciuis to fehranheight
# def convert(c):
    # return (c * 9/5)+32

# convert=lambda num:(num*9/5)+32
# print(convert(10))
#write a function that takes a list of number and returns a new list with each number squared but skip any negative numbers.
#[2,-1,10,-5]=>[4,-1,100,-5]
x=[2,-1,10,-5]
# def square(list):
#    new_list=[]
#    for x in list:
    #   if x>=0:
        # new_list.append(x**2)
    #   else:
        #  new_list.append(x)
#    return new_list
# result=square(x)
# print(result)
# def squared(list):
    # for i,num in enumerate(list):
        # if num <0:
            # continue
        # else:
            # list[i]=num**2
    # return list
# print(squared([2,-1,10,-5]))
#recursive function
# def f1(x):
    #SOMETHING THAT STOPS THE RECURSION
    #BASE CASE
    # return f1(x-1)
#rules if writing a recursive function
# 1- have a  base case to prevent infinte loops
# 2- at least 1 argumant must change when calling the function
# conter=10
# for i in range (10,0,-1):
    # print(i)

# def countdown(counter):
    # if counter == 0:
        # return
    # print(counter)
    # countdown(counter-1)
# countdown(10)
#write a recursive function that calculate the sum from 0 to n

# def sum_to_n(n):
    # if n==0:
    #    return 0
    # return (n + sum_to_n(n-1))
# print(sum_to_n(10))
def factorial(n):
    if n==0:
       return 0
    return (n *factorial(n-1))
print(factorial(10))





