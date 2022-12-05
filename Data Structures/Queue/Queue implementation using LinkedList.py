class Node : 
    def __init__ (self, value): 
        self.value = value 
        self.next = None 

class Queue : 

    def __init__(self): 
        self.head = None 
    
    def __str__(self) : # print the queue 
        if self.head is None : 
            return "Queue is Empty"
        else : 
            itr = self.head 
            llst = ""
            while itr : 
                llst += str(itr.value) + " " if itr.next else str(itr.value)                  
                itr = itr.next 
            return llst    
    
    def __len__(self) : # size of queue
        count = 0 
        itr = self.head 
        
        while itr : 
            itr = itr.next 
            count += 1 
        return count 
                        
    # push
    def enqueue(self, value) :  
        if self.head is None : 
            self.head = Node(value)  
        
        else :      
            itr = self.head         
            while itr.next :           
                itr = itr.next  
            itr.next = Node(value) 
                
    # removes the first element of the queue    
    def dequeue(self)  :  
        self.head = self.head.next
        return "First item is deleted"
        
        
    # prints the size of queue       
    def size(self) : 
        print(len(self))
        
        
    # print True is queue is empty else
    # print False    
    def isEmpty(self) : # is empty function 
        if self.head == None: 
            print (True) 
        else : 
            print (False) 
     
                   
    # returns the top element of the queue        
    def peek(self) :  
        print (self.head.value)
  
        
    # deletes the entire queue     
    def delete (self) : 
        self.head = None 
        return "Queue is deleted"
        
    def printQueue(self) : # print the queue 
        if self.head is None : 
            print("Queue is Empty")
        else : 
            itr = self.head 
            llst = ""
            while itr : 
                llst += str(itr.value) + " " if itr.next else str(itr.value)                  
                itr = itr.next 
            print(llst) 
            
            
# instances of Queue       
q = Queue ()
