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
#linked list implementation of queue
#CHAINED LIST
class linked_list:
    def __init__(self):
         self.head=None
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
        def append(self,new_node):#add new node to the end of the linked list
            current=self.head
            if current:
                while current.next:
                     current=current.next
                current.next=self.new_node
            else:
                    self.head=new_node
        def display(self):#display the linked list
            current=self.head
            while current:
                print(current.data)
                current=current.next
        def delete(self,value):#delete a node from the linked list
                current=self.head
                if current:
                    if current.data==value:
                        self.head=current.next
                        current=None
                        return
                while current:
                    if current.data==value:
                        break
                    prev=current
                    current=current.next
                if current is None:
                    return
                prev.next=current.next
                current=None
                def insert(self,new_node,position):#insert a new node at a given position
                    current=self.head
                    if position==0:
                        new_node.next=self.head
                        self.head=new_node
                        return
                    count=0
                    while current:
                        if count==position:
                            break
                        prev=current
                        current=current.next
                        count+=1
                    if current is None:
                        prev.next=new_node
                        return
                    prev.next=new_node
                    new_node.next=current

    