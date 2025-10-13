#stacks quues and priority queues
#stack is a data structure that follows the LIFO (last in first out) principle is a list 
#queue is a data structure that follows the FIFO (first in first out) principle
#priority queue is a data structure that follows the priority principle (the element with the highest priority is served before the other elements)
class Stack:
    def __init__(self,stack:list=[]):
        self.stack=stack
    def push(self,item):
       self.stack.append(item)
    def pop(self):

       return self.new_method()

    def new_method(self):
        if self.is_empty():
             print("stack is empty")
        return self.stack.pop()
    def peek(self):
       return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0 
my_stack=Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack.stack)
my_stack.pop()
print(my_stack.stack)
print(my_stack.peek())
print(my_stack.is_empty())
my_stack.pop()
my_stack.pop()
my_stack.pop()
class Queue:
    def __init__(self,queue:list=[]):
        self.queue=queue
    def enqueue(self,item): #add item to the end of the queue
       self.queue.append(item)
    def dequeue(self):#remove item from the front of the queue
       if self.is_empty():
             print("queue is empty")
       return self.queue.pop(0)
    def peek(self): #return the first item in the queue
       return self.queue[0]
    def is_empty(self):#check if the queue is empty
        return len(self.queue) == 0