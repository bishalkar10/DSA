class Node : 
    def __init__ (self, value): 
        self.value = value 
        self.next = None 

class Stack : 
    def __init__(self): 
        self.head = None 
    
    def __str__(self) : # print the stack
        if self.head is None : 
            return "Stack is Empty"
        else : 
            itr = self.head 
            llst = ""
            while itr : 
                llst += str(itr.value) + " " if itr.next else str(itr.value)                  
                itr = itr.next 
            return llst    
    
    def __len__(self) : # size of stack
        count = 0 
        itr = self.head 
        
        while itr : 
            itr = itr.next 
            count += 1 
        return count 
                        
    # push
    def push(self, value) :        
        new_Node = Node(value)
        new_Node.next = self.head 
        self.head = new_Node 
    
    # removes the top element of the stacks    
    def remove(self)  :  
        self.head = self.head.next
     
    # prints the size of stack       
    def size(self) : 
        print(len(self))
        
    # print True is stack is empty else
    # print False    
    def isEmpty(self) : # is empty function 
        if self.head == None: 
            print (True) 
        else : 
            print (False) 
            
    # returns the top element of the stack        
    def peek(self) :  
        print (self.head.value)
        
    # returns the top element of the stack
    def top(self) : 
        print (self.head.value)  
        
    # deletes the entire stack     
    def delete(self) : 
        self.head = None 
    
    def printStack(self) : # print the stack
        if self.head is None : 
            print("Stack is Empty")
        else : 
            itr = self.head 
            llst = ""
            while itr : 
                llst += str(itr.value) + " " if itr.next else str(itr.value)                  
                itr = itr.next 
            print(llst)
    
# instance of Stack      
stack = Stack()
