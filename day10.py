#stacks quues and priority queues
#stack is a data structure that follows the LIFO (last in first out) principle is a list 
#queue is a data structure that follows the FIFO (first in first out) principle
#priority queue is a data structure that follows the priority principle (the element with the highest priority is served before the other elements)
# class Stack:
#     def __init__(self,stack:list=[]):
#         self.stack=stack
#     def push(self,item):
#        self.stack.append(item)
#     def pop(self):

#        return self.new_method()

#     def new_method(self):
#         if self.is_empty():
#              print("stack is empty")
#         return self.stack.pop()
#     def peek(self):
#        return self.stack[-1]
#     def is_empty(self):
#         return len(self.stack) == 0 
# my_stack=Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# print(my_stack.stack)
# my_stack.pop()
# print(my_stack.stack)
# print(my_stack.peek())
# print(my_stack.is_empty())
# my_stack.pop()
# my_stack.pop()
# my_stack.pop()
# class Queue:
#     def __init__(self,queue:list=[]):
#         self.queue=queue
#     def enqueue(self,item): #add item to the end of the queue
#        self.queue.append(item)
#     def dequeue(self):#remove item from the front of the queue
#        if self.is_empty():
#              print("queue is empty")
#        return self.queue.pop(0)
#     def peek(self): #return the first item in the queue
#        return self.queue[0]
#     def is_empty(self):#check if the queue is empty
#         return len(self.queue) == 0
#linked list implementation of queue
#CHAINED LIST
class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
class linked_list:
    def __init__(self):
                self.head=None

    def insert_at_beginning(self,value):
        new_node=Node(value)
        if self.head == None:
            self.head = new_node
            return
        new_node.next=self.head
        self.head=new_node
        return
    
    def insert_at_end(self,value):
        
        
        
        if self.head ==None:
            self.insert_at_beginning(value)
            return
            
        new_node=Node(value)
        curr=self.head
        
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        return
    def display(self):#display the linked list
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def delete_value(self,value):     
            if self.head == None:
                return 
            elif self.head.data==value:
                 self.head=self.head.next
                 return
            curr= self.head
            found =False
        
            while curr.next!=None:
                
                if curr.next.data==value:
                    found=True        
                    break
                curr=curr.next
            
            if found == True:
                curr.next=curr.next.next
                return
    def search(self,value):
            
            if self.head ==None:
                return
            
            curr=self.head
            
            while curr!=None:
                if curr.data==value:
                    return True
                curr=curr.next
            
            return False
l=linked_list()
l.insert_at_end(1)
l.insert_at_end(5)
l.insert_at_end(555)

l.delete_value(1)
l.display()