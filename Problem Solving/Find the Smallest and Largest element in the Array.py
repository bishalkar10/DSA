"""
Find Largest and Smallest number in Unsorted array :
"""
import random 

Array = [x for x in range (0,101)]

random.shuffle(Array)

print ("Naive Method")
print ("Time Complexity : 0(n)")
print ()
Smallest_Number = Array[0] 
Biggest_Number = Array[len(Array)-1]

for item in Array : 
    if item > Biggest_Number : 
        Biggest_Number = item
    elif item < Smallest_Number : 
        Smallest_Number = item

print ("Smallest_Number", Smallest_Number)

print ("Biggest_Number", Biggest_Number) 
print ()
print ("Method 2 : Sort The Array") 
print()
Array.sort() 
print ("Smallest_Number", Array[0])

print ("Biggest_Number", Array[len(Array)-1]) 
print ()

print ("Method 3 : ") 

print ("Smallest_Number", min(Array)) 
print ("Biggest_Number", max(Array)) 

