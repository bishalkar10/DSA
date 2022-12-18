""" 
Given a string S, the task is to find the bracket numbers. 
User Task:
Your task is to complete the function barcketNumbers() 
which takes a single string as input and returns a list of numbers. 
You do not need to take any input or print anything.
"""  

""" 
Link : https://practice.geeksforgeeks.org/problems/print-bracket-number4058/1?page=2&category[]=Stack&sortBy=submissions
"""

def bracketnumbers(self, S):
		# code here 
  # We will store answer here..
		List = [] 
  # we will store number of brackets
		Stack = []
  # mark the opening bracket with i
		i = 1
  # Traversing String 
		for char in S : 
      # if character is 
		    if char is "(" : 
		        List.append(i) 
		        Stack.append(i)  
      # if "(" is found then increase i by 1
		        i+= 1
      # closing brackets value will be the 
      # the equal of last opening bracket 
		    if char is ")" : 
		        List.append(Stack.pop()) 
		    
		return List
