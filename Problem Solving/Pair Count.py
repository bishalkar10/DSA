"""
Given an Array of integers find out how many pair of integers 
are in the array which sum is equal to a target number. 
"""

"""  
Link : https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1
"""
# import collection 
from collections import Counter 

def Pair(arr, Sum):
    # varibale that store Pair number
    Pair = 0 
    # Dictionary for storing Element count
    myDict = Counter(arr) 
    # for elements in array
    for item in arr :  
        myDict[item] -= 1 
        # if (Sum-element) is number to find in myDict      
        if (Sum - item) in myDict : 
        # How many Sum- element in dictionary?
            Pair += myDict[Sum-item]
    return Pair   
      
arr = [1,1,1,1] 
Sum= 2

# Approach 2 : without collections Module....
def getPairsCount(arr, n, Sum):  
    # create an empty Dictionary 
    myDict = {}
    count = 0
    
    for item in arr: 
        # if value is in Dictionary 
        if Sum - item in myDict:
            count += myDict[Sum - item]
        
        if item in myDict:
            myDict[item] += 1
        
        else:
            myDict[item] = 1
    
    return count

