# traversing the binary tree non-recursively with the help of a stack


#stack
class Stack(object):
    def __init__(self,len):
        self.stack_array=[None for i in range(len)]
        self.max_length=len
        self.current_length=0
    def push(self,value):
        if self.current_length==self.max_length:
            print "overflow"
            return False
        else:
            self.current_length+=1
            self.stack_array[self.current_length-1]=value
            return True

    def pop(self):
        if self.current_length==0:
            print "underflow"
            return False
        else:
            self.current_length-=1
            return self.stack_array[self.current_length]

    def isEmpty(self):
        if self.current_length==0:
            #print "stack is empty"
            return True
        else:
            #print "stack is not empty"
            return False


# binary tree
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

    def display_nonrecurive_preorder(self):  # preorder traversal
        s=Stack(2**(self.depth+1)-1)
        iter=self.root
        while (iter.left!=None)or(iter.right!=None):
            print iter.key
            if iter.right!=None:
                s.push(iter.right)
            if iter.left!=None:
                iter=iter.left
        print iter.key
        while not(s.isEmpty()):
            iter=s.pop()
            while (iter.left!=None)or(iter.right!=None):
                print iter.key
                if iter.right!=None:
                    s.push(iter.right)
                if iter.left!=None:
                    iter=iter.left
            print iter.key

        '''
        s=Stack(2**(self.depth+1)-1)
        iter=self.root
        while (iter.left!=None)or(iter.right!=None)or(not s.isEmpty()):
            if (iter.left!=None)or(iter.right!=None):
                print iter.key
                if iter.right!=None:
                    s.push(iter.right)
                if iter.left!=None:
                    iter=iter.left
            else:
                print iter.key
                iter=s.pop()
        print iter.key
        '''

# test code
'''
ss=Stack(5)
ss.pop()
ss.push(1)
ss.push(2)
ss.push(3)
print ss.pop()
print ss.pop()
print ss.pop()
'''
b=BinaryTree()
b.create_recurive(3)
b.display_nonrecurive_preorder()


