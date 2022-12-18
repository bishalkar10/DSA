"""
Find the missing number in array :
"""
import random 

arr = [x for x in range (1,101) ] 

del arr[random.randint(1,100)]

Max_num = max(arr)

Number = Max_num* (Max_num+1)//2 - sum(arr)
print ("The missing number is : ")
print (Number)
