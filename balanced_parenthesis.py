print("********Balanced Parenthesis*********")
class Stack:
    
    #Initialized the list element
    def __init__(self):
        self.items = []
 
    #Checking stack is empty or not
    def is_empty(self):
        return self.items == []
    
    #Add elements in the stack 
    def push(self, data):
        self.items.append(data)
 
    #Delete element from stack
    def pop(self):
        return self.items.pop()
 
#Object of stack
stack = Stack()

#Taking input from user
expression = input('Please enter the expression: ')

#Traversing the expression
for index in expression:
    if index == '(':
        #Add element to the stack
        stack.push(1)
    elif index == ')':
        if stack.is_empty():
            is_balanced = False
            break
        else:
            #Delete element from the stack
            stack.pop()
    else:
        if stack.is_empty():
            is_balanced = True
        else:
            is_balanced = False

#Check expression is balanced or not
if is_balanced:
    print('Expression is correctly parenthesized.')
else:
    print('Expression is not correctly parenthesized.')
