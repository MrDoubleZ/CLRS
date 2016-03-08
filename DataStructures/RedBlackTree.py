# red black tree

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


class node(object):
    def __init__(self,val):
        self.key=val
        self.left=None
        self.right=None
        self.parent=None
        self.color=None


class RedBlackTree(object):
    def __init__(self):
        self.root=None
        self.nil=node(None)

    def search(self,val):
        if self.root==None:
            return None
        x=self.__search__(val,self.root)
        if x==self.nil:
            return None
        else:
            print "find it!"
            return x

    def __search__(self,val,n):
        x=n
        while x!=self.nil and val!=x.key:
            if val<x.key:
                self.__search__(val,x.left)
            else:
                self.__search__(val,x.right)
        return x

    def inorder_tree_walk_nonrecursive(self):
        if self.root==None:
            print "the red black tree is empty!"
        x=self.root
        s=Stack(10)  # the rbtree's height is 10 at most
        while (not s.isEmpty())or(not x!=self.nil):
            if x!=self.nil:
                s.push(x)
                x=x.left  # x maybe nil in this operation
            else:  # x.left==self.nil, so in this branch, isEmpty() return False
                x=s.pop()
                print x.key
                x=x.right

    def transplant(self,u,v):  # replace u and its subtree with v and its subtree
        if u.parent==self.nil:
            self.root=v
        elif u.parent.left==u:
            u.parent.left=v
        else:
            u.parent.right=v
        v.parent=u.parent

    def min(self,n):
        x=n
        while x.left!=self.nil:
            x=x.left
        return x.key

    def max(self,n):
        x=n
        while x.right!=self.nil:
            x=x.right
        return x.key

    def successor(self,n):
        x=n
        if x.right!=self.nil:
            return self.min(x.right)
        else:
            while x.parent!=self.nil and x.parent.left!=x:
                x=x.parent
            return x.parent  # if n==max(self,root), it will return root's parent self.nil

    def predecessor(self,n):
        x=n
        if x.left!=self.nil:
            return self.max(x.right)
        else:
            while x.parent!=self.nil and x.parent.right!=x:
                x=x.parent
            return x.parent  # if n==min(self,root), it will return root's parent self.nil

    def insert(self,val):
        pass

    def delete(self,val):
        pass
