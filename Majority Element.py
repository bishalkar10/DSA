"""
Given an array A of N elements.
Find the majority element in the array. 
A majority element in an array A of size N 
is an element that appears more than N/2 times in the array.
"""

"""
Link : https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&sortBy=submissions
"""
def majority_element(A,N):
        #Your code here 
        if N == 1 : 
            return A[0] 
        elif N == 0 : 
            return -1
        # An empty Dictionary from storing 
        # unique item frequency
        Dict = {} 
        # iterating through Array
        for item in A : 
        # If item is present in Dictionary 
            if item in Dict : 
            # increase value by 1
                Dict[item] += 1 
            else : # Else add Key : Pair
                Dict[item] = 1 
        # iterating through Array
        for item in A : 
        # If item is present more than half of the array 
        # return item
            if Dict[item] > N/2 : 
                return item
        return -1 
"""
If we just use Counter from collections Module 
we can reduce Some code 
"""
# approach 2 
from collections import Counter 

def Majority_Element(A,N):
        #Your code here 
        if N == 1 : 
            return A[0] 
        elif  N == 0 : 
            return -1
            
        Dict = Counter (A)
         
        for item in A :
            if Dict[item] > N/2 : 
                return item
        return -1 