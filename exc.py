#git init
#git add .
#git commit -m "Initial commit"
#git remote add origin
#git push -u origin master
# x=19
# print("guess a number between 1 and 20")
# y=int(input("enter your guess :"))
# while y!=x:
    # # if y<x:
    #     print("too low")
        # y=int(input("enter your guess :"))
    # elif y>x:
        # print("too high")
        # y=int(input("enter your guess :"))
# else:
    # print("you guessed it right")
x=28
print("pls guess the number")
t=int(input("enter yout guessed number :"))
while t!=x:
    if t<x:
        print("it is lower")
        t=int(input("enter yout guessed number :"))
    elif t>x:
        print("it is high ")
        t=int(input("enter yout guessed number :"))
else:
 print("that is correct")  
   
 #casting
#int() float() str() list() tuple() set() dict()
# a="123"