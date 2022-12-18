# Reverse a linked list  
""" 
https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1?page=2&sortBy=submissions
"""

def reverseList(self, head):
        List = [] 
        itr = head

        while itr : 
            List.append(itr.data) 
            itr = itr.next 
            
        itr = head 
        
        while itr : 
            itr.data = List.pop() 
            itr = itr.next 
            
        return head
