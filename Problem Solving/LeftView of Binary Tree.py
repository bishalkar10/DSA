""" 
Given a Binary Tree, print Left view of it. Left view of a Binary Tree is set of nodes visible when tree is visited from Left side. The task is to complete the function leftView(), which accepts root of the tree as argument.

Left view of following tree is 1 2 4 8.

          1
       /     \
     2        3
   /   \    /   \
  4     5  6     7
   \
    8   
    
Input oder is in lever order    
Input for this Tree is : 1,2,3,4,5,6,7,None,8
""" 


def LeftView(root):
    # A Dictionary to store level : fisrt item value pair
    Dict = {} 
    # In this list we will store out answer
    List = [] 
    # A mini and helper BFS 
    def solve (root, level ) : 
        if root is None : 
            return 
        if level not in Dict : 
            Dict[level] = root.data 
        solve(root.left, level +1) 
        solve(root.right, level +1)
    # Calling the function, level is 1    
    solve(root, 1)
    #  sorting the dictionary by value 
    for key, value in sorted(Dict.items()) : 
        List.append(value) 
    
    return List
    
# Approach 2 
""" 
Suppose There is a tree  Like this Below code will 
print : 1,2  
Below code is somewhere faulty . It's my original Idea.
while above code can print : 1,2,4,6
             1 
           /   \
          2     3 
              /   \
             4     5 
           /   \  
          6     7
        
""" 
def leftview(root) : 
    # List for storing values of root.data
    List = [] 
    # a nested helper function
    def helper(root) : 
        # if root is not None 
        if root is not N : 
        
            List.append(root.data) 
            if root.left : 
            # change root parameter to root.left
                helper(root.left) 
            else : 
            # change root parameter to root.right
                helper(root.right) 
    # Calling helper function 
    helper(root) 
    return List




