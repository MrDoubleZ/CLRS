# traversing the binary tree recursively, traversal order: left-right-middle

class node(object):
    def __init__(self,val,n):
        self.key=val
        self.left=None
        self.right=None
        self.parent=n

class BinaryTree(object):
    def __init__(self):
        self.root=node(None,None)
        self.depth=None
        self.count=0

    def __create_recurive__(self,depth,n):# order left-right top-down
        if depth!=0:
            n.left=node(self.count,n)
            self.count+=1
            n.right=node(self.count,n)
            self.count+=1
            self.__create_recurive__(depth-1,n.left)
            self.__create_recurive__(depth-1,n.right)
        return
    def create_recurive(self,depth):
        self.depth=depth
        self.__create_recurive__(depth,self.root)

    def __display_recurive__(self,depth,n):
        if depth!=0:
            self.__display_recurive__(depth-1,n.left)
            self.__display_recurive__(depth-1,n.right)
        print n.key

    def display_recurive(self):# left order traverse
        self.__display_recurive__(self.depth,self.root)



# test code
b=BinaryTree()
b.create_recurive(3)
b.display_recurive()