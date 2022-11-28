# Bubble Sort Implementation 

import random # importing random Module

# using list comprehension to create a list

array = [x for x in range (1,1001)] 

random.shuffle(array) # shuffling the list

def Bubble_Sort(arr) : # defining starts

    size = len(array) # size of array

    # if not a single element got swapped then

    # the rest of the list is sorted. This saves time.

    swapped = False  

    # we have to perform size -1 iteration

    for i in range (size-1) :  

       # as after each iteration the biggest element

       # get in the last position, so we will do

       # one less iteration each time..

       for j in range (size-1-i) : 

       # if left side element is greater than right one 

            if array[j] > array[j+1] :

                 # then we swap

                array[j], array[j+1] = array[j+1], array[j] 

                swapped = True 

       if not swapped : # if none element got swapped 

           return      # then return 

Bubble_Sort(array) # calling function 

print ("Sorted is :")

print (array)# printing the sorted array..
