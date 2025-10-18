input_name = input("pls enter your name: ")
class1 = int(input("pls enter your class: "))
grade = int(input("pls enter your grade: "))
def greet( input_name,class1,grade):
    if grade >= 50:
        print("congratulation mr/mrs",input_name," you have been promoted 1 class up",class1+1)
    else:
        print("we regret to tell mr/mrs",input_name,"you that you will stay in your class",int(class1))
greet(input_name,class1,grade)

