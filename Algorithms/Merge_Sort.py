def merge_sort(nums) :
    
    # if list has 1 or 0 element return the list
    if len (nums) < 2 : 
        return nums
   
    # mid index of list  
    mid = len (nums) //2 
    
    # split the list into two list
    left = nums[:mid] 
    right = nums[mid:] 
    
    # use merge_sort recusively 
    left_sorted , right_sorted = merge_sort(left), merge_sort(right)
    
    # call merge function to merge two sorted list
    return merge(left_sorted, right_sorted)
    
    
def merge (nums1, nums2) : 

    # initiating indices for iterating and
    # empty list for storing values
    i,j,merged = 0,0,[] 
    
    # while indices are less than list length 
    while i < len(nums1) and j < len(nums2) : 
        
        # append smaller elements in merge list 
        # and move on to next index
        if nums1[i] <= nums2[j] : 
            merged.append(nums1[i]) 
            i += 1 
        else : 
            merged.append(nums2[j]) 
            j += 1
    
    # remaining list
    nums1_tail = nums1[i:] 
    nums2_tail = nums2[j:] 
    
    # combine merged list and remaining list
    return merged + nums1_tail + nums2_tail

# driver code     
if __name__ == "__main__" : 

    import random

    List = [i for i in range (1, 11)] 
    random.shuffle(List)
    print (List)
    print ()

    print ("After sorting")
    print (merge_sort(List) )

