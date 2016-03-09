# binary search tree
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


class node(object):
    def __init__(self,val):
        self.key=val
        self.left=None
        self.right=None
        self.parent=None


class BinarySearchTree(object):
    def __init__(self):
        self.root=None

    def insert(self,val):
        y=None
        x=self.root
        n=node(val)
        while x!=None:  # run one time at least, because BinarySearchTree has one node(root node) at least
            y=x
            if val<x.key:
                x=x.left
            else:
                x=x.right
        n.parent=y
        if y==None:
            self.root=n
        elif val<y.key:
            y.left=n
        else:
            y.right=n

    def __insert_recursive__(self,v,n):
        if n==None:  # tree has no node
            self.root=v
        else:
            if v.key<n.key:
                if n.left!=None:
                    self.__insert_recursive__(v,n.left)
                else:
                    n.left=v
                    v.parent=n
            else:
                if n.right!=None:
                    self.__insert_recursive__(v,n.right)
                else:
                    n.right=v
                    v.parent=n

    def insert_recursive(self,val):
        n=node(val)
        self.__insert_recursive__(n,self.root)

    def __inorder_tree_walk_recursive__(self,n):
        if n.left!=None:
            self.__inorder_tree_walk_recursive__(n.left)
            print n.key
        else:
            print n.key
        if n.right!=None:
            self.__inorder_tree_walk_recursive__(n.right)

    def inorder_tree_walk_recursive(self):
        self.__inorder_tree_walk_recursive__(self.root)

    def inorder_tree_walk_nonrecursive(self):  # the idea of state machine
        '''
        state1: curr.left==prev
        state2: prev.left==curr
        state3: curr.right==prev
        state4: prev.right==curr
        '''
        curr=self.root
        if curr.left!=None:
            prev=curr
            curr=curr.left
        elif curr.right!=None:
            prev=curr
            curr=curr.right
        else:
            print curr.key
        while curr!=None:
            if curr.left==prev:  # state1
                #print "state1"
                print curr.key
                if curr.right!=None:  # change to state4
                    prev=curr
                    curr=curr.right
                else:
                    prev=curr
                    curr=curr.parent

            if prev.left==curr:  # state2
                #print "state2"
                if curr.left!=None: # change to state2
                    prev=curr
                    curr=curr.left
                else:
                    print curr.key
                    if curr.right!=None: # change to state4
                        prev=curr
                        curr=curr.right
                    else:
                        prev=curr
                        curr=curr.parent

            if curr.right==prev: # state3
                #print "state3"
                prev=curr
                curr=curr.parent

            if prev.right==curr: # state4
                #print "state4"
                if curr.left!=None: # change to state2
                    prev=curr
                    curr=curr.left
                else:
                    print curr.key
                    if curr.right!=None: # change to state4
                        prev=curr
                        curr=curr.right
                    else:
                        prev=curr
                        curr=curr.parent

    def search_nonrecursive(self,val):
        x=self.root
        while x!=None and x.key!=val:
            if val<x.key:
                x=x.left
            else:
                x=x.right
        return x

    def __search_recursive__(self,val,n):
        '''
        if n.key==val:
            return n
        elif val<n.key:
            return self.__search_recursive(val,n.left)
        else:
            return self.__inorder_tree_walk_recursive(val,n.right)
        return n
        '''
        if n!=None and n.key!=val:
            if val<n.key:
                return self.__search_recursive__(val,n.left)
            else:
                return self.__inorder_tree_walk_recursive__(val,n.right)
        else:
            return n

    def search_recursive(self,val):
        x=self.root
        return self.__search_recursive__(val,x)

    def transplant(self,u,v):  # if u==root and v==None, the procedure will replace the binary search tree's root with None!
        parent=u.parent
        if parent==None:
            self.root=v
        elif parent.left==u:
            parent.left=v
        else:
            parent.right=v
        if v!=None:
            v.parent=parent

    def min(self,n):
        x=n
        while x!=None:
            y=x
            x=x.left
        return y

    def min_recursive(self,n):
        if n.left!=None:
            return self.min_recursive(n.left)
        else:
            return n

    def max(self,n):
        x=n
        while x!=None:
            y=x
            x=x.right
        return y

    def successor(self,n):
        if n.right!=None:
            return self.min(n.right)
        else:
            y=n.parent
            x=n
            while y.right==x and y!=None:
                x=y
                y=y.parent
            return y

    def predecessor(self,n):
        if n.left!=None:
            return self.max(n.left)
        else:
            y=n.parent
            x=n
            while y.left==x and y!=None:
                x=y
                y=y.parent
            return y

    '''
    def delete(self,n):
        if n.left==None:
            self.transplant(n,n.right)
        elif n.right==None:
            self.transplant(n,n.left)
        else:
            y=self.min(n.right)
            if y.parent!=n:
                self.transplant(y,y.right)
                n.right.parent=y
                y.right=n.right
            self.transplant(n,y)
            n.left.parent=y
            y.left=n.left
    '''

    def delete(self,x):  # a little different from CLRS
        if x.right==None:
            self.transplant(x,x.left)
        else:
            y=self.min(x.right)
            if y!=x.right:
                self.transplant(y,y.right)
                x.right.parent=y
                y.right=x.right
            self.transplant(x,y)
            x.left.parent=y
            y.left=x.left
            y.parent=x.parent

    def delete_find_predecessor(self,n):
        if n.left==None:
            self.transplant(n,n.right)
        elif n.right==None:
            self.transplant(n,n.left)
        else:
            y=self.max(n.left)  # predecessor
            if y.parent!=n:
                self.transplant(y,y.left)
                n.left.parent=y
                y.left=n.left
            self.transplant(n,y)
            n.right.parent=y
            y.right=n.right

    def reverse(self):
        pass


# test code
bst=BinarySearchTree()

bst.insert_recursive(12)

bst.insert(5)
bst.insert(18)
bst.insert(2)
bst.insert(9)
bst.insert_recursive(15)
bst.insert_recursive(19)
bst.insert_recursive(13)
bst.insert_recursive(17)


bst.inorder_tree_walk_nonrecursive()   # 2 5 9 12 13 15 17 18 19


print bst.max(bst.root).key  # 19
print "min_recursive: %d" %bst.min_recursive(bst.root).key  # 2
print bst.successor(bst.root).key # 13
print bst.successor(bst.root.left.right).key  # 12
print bst.predecessor(bst.root).key  # 9
print bst.predecessor(bst.root.right.left.left).key  # 12


bst.delete(bst.root.right.left)  # delete 15
bst.delete(bst.root.right.left)  # delete 17
bst.delete(bst.root.right.left)  # delete 13


bst.inorder_tree_walk_recursive()
