class TreeNode (): # 
    def __init__ (self, data) : #intializer
        self.data = data  # assigning data
        self.children = [] # children list
        self.parent = None 

    def getLevel(self) : 
        level = 0 
        p = self.parent  
        while p : 
            level += 1 
            p = p.parent
        
        return level

    def print_tree(self):
        
        spaces = " " * self.getLevel() * 3 
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+ self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def Product_Tree():
    # Creating instances of TreeNode 
    #Root Node is "Electronics"
    root = TreeNode("Electronics")
    
    # Child of root - Level 1 Node   
    cto = TreeNode("CTO")  
    
    # Child of cto - Level 2 Node
    infra_head = TreeNode("Infrastructure Head")
    
    # Child of infra_head - Level 3 Node
    cloud_manager = TreeNode("Cloud Manager")
    
    # child of infra_head - Level 3 Node 
    app_manager = TreeNode("App Manager")
    
    # Child of cto - Level 3 Node
    application_head = TreeNode("Application Head")
    
    # child of root - level 1 Node
    hr_head = TreeNode("HR Head")
    
    # child of hr_head - Level 2 Node
    recruiting_manager = TreeNode("Recruiting Manager")
    
    # child of hr_head - Level 2 Node
    policy_manager = TreeNode("Policy Manager") 
    
    infra_head.add_child(app_manager)
    
    infra_head.add_child(cloud_manager)
    
    cto.add_child(infra_head) 
    
    cto.add_child(application_head)
    
    hr_head.add_child(recruiting_manager)
   
    hr_head.add_child(policy_manager)
    
    root.add_child(cto)
    
    root.add_child(hr_head)
    
    root.print_tree() # print tree

Product_Tree()
