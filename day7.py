x=5
y=10
z=x+y
#some more codes
t=15 
g=20 

r= t+g
#function
#the yare of piece of code that is used multiple times throughout the program
#define a function telling your pogram that this piece of code is ready to be used at any time
# def add_numbers(a,b):
    # return a+b
# input_name = input("Enter your name: ")
# def greet(input_name):
    # print("Hello, " + input_name + ". How are you?")
# greet(input_name)
# def greet(name,age=None, Grade=None):
    # print("Hello, " + name + ". How are you?")
    # if age is not None:
        # print("You are " + str(age) + " years old.")
    # if Grade is not None:
        # print("You are in grade " + Grade + ".")
# 
    # print("Hello, " + name + ". How are you?")
# greet("Alice", age=30, Grade="A")
# greet("Bob", Grade="B")
# greet("Charlie", age=25)
def add(a,b):
    return a+b
#what if i want to return more than one value
def add_subtract(a,b):
    return a+b, a-b
result_add, result_subtract = add_subtract(10,5)
print("Addition:", result_add)
print("Subtraction:", result_subtract)
#return multiple values as a tuple
def add_subtract_multiply(a,b):
    return a+b, a-b, a*b
result = add_subtract_multiply(10,5)
print("Addition:", result[0])
print("Subtraction:", result[1])
print("Multiplication:", result[2])
