# Leetcode Problems 1 : Two Sum 

def twoSum(nums, target ) : 
    # a hashmap for storing num indexes as values
    Dictionary = {} 
    for i in range (len(nums)) :
     
        val = target - nums[i] 
        if val in Dictionary : 
            return [Dictionary[val], i]  
        Dictionary[nums[i]] = i
        
        
nums = [2,7,5,1,10,1] 
target = 11
print (twoSum(nums, target)) 
