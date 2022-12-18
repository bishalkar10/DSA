"""
Find Duplicate number in List :
"""
my_list= [1,1,2,3,4,6,7,9,5,7,9,8,0,76,5,4,23,45,67,45,23,21,89,67,54]


print ("Method : 1 ") 
for i in range(0, len(my_list)):
   for j in range(i+1, len(my_list)):
      if(my_list[i] == my_list[j]):
         print(my_list[j])  
 
print ()

print ("Method :2" )
Duplicates_List =[] 

for i in my_list : 
    if my_list.count(i) > 1 and i not in Duplicates_List : 
        Duplicates_List.append(i)
        
print (Duplicates_List)