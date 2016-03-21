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
        self.color=None  # black==0, red==1

        self.size=1


class RedBlackTree(object):
    def __init__(self):
        self.nil=node(None)
        self.nil.color=0
        self.root=self.nil
        self.nil.size=0

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
                x=self.__search__(val,x.left)
            else:
                x=self.__search__(val,x.right)
        return x

    def inorder_tree_walk_nonrecursive(self):
        if self.root==None:
            print "the red black tree is empty!"
        x=self.root
        s=Stack(10)  # the rbtree's height is 10 at most
        while (not s.isEmpty())or(x!=self.nil):
            if x!=self.nil:
                s.push(x)
                x=x.left  # x maybe nil in this operation
            else:  # x.left==self.nil, so in this branch, isEmpty() return False
                x=s.pop()
                print "key:%d, color:%d, size:%d" %(x.key,x.color,x.size)
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
        while x!=self.nil:
            y=x
            x=x.left
        return y

    def max(self,n):
        x=n
        while x!=self.nil:
            y=x
            x=x.right
        return y

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

    def insert_fixup(self,z):
        while z.parent.color==1:
            if z.parent==z.parent.parent.left:
                y=z.parent.parent.right
                if y.color==1:
                    y.color=0
                    z.parent.color=0
                    z.parent.parent.color=1
                    z=z.parent.parent
                else:
                    if z==z.parent.right:
                        z=z.parent
                        self.left_rotate(z)
                    z.parent.parent.color=1
                    self.right_rotate(z.parent.parent)
            else:
                y=z.parent.parent.left
                if y.color==1:
                    y.color=0
                    z.parent.color=0
                    z.parent.parent.color=1
                    z=z.parent.parent
                else:
                    if z==z.parent.left:
                        z=z.parent
                        self.right_rotate(z)
                    z.parent.color=0
                    z.parent.parent.color=1
                    self.left_rotate(z.parent.parent)
        self.root.color=0

    def left_rotate(self,n):
        x=n
        y=n.right
        if x==self.root:
            self.root=y
        elif x==x.parent.left:
            x.parent.left=y
        else:
            x.parent.right=y
        y.parent=x.parent
        x.right=y.left
        if y.left!=self.nil:
            y.left.parent=x
        y.left=x
        x.parent=y
        y.size=x.size
        x.size=x.left.size+x.right.size+1

    def right_rotate(self,n):
        x=n
        y=n.left
        if x==self.root:
            self.root=y
        elif x==x.parent.right:
            x.parent.right=y
        else:
            x.parent.left=y
        y.parent=x.parent
        x.left=y.right
        if y.right!=self.nil:
            y.right.parent=x
        y.right=x
        x.parent=y
        y.size=x.size
        x.size=x.left.size+x.right.size+1

    def delete_fixup(self,n):
        x=n
        while x!=self.root and x.color==0:
            if x==x.parent.left:
                w=x.parent.right
                if w.color==1:  # it can indicate that x.parent(w.parent).color==black
                    w.color=0
                    x.parent.color=1
                    self.left_rotate(x.parent)
                    w=x.parent.right
                if w.left.color==0 and w.right.color==0:
                    w.color=1
                    x=x.parent
                else:
                    if w.right.color==0:
                        w.left.color=0
                        w.color=1
                        self.right_rotate(w)
                        w=x.parent.right
                    w.color=x.parent.color
                    x.parent.color=0
                    w.right.color=0  # because x.parent will be rotated to be w's child, w.right's black height will
                                    # decrease by 1. thus recolor it to black
                    self.left_rotate(x.parent)
                    x=self.root
            else:
                w=x.parent.left
                if w.color==1:  # it can indicate that x.parent(w.parent).color==black
                    w.color=0
                    x.parent.color=1
                    self.right_rotate(x.parent)
                    w=x.parent.left
                if w.right.color==0 and w.left.color==0:
                    w.color=1
                    x=x.parent
                else:
                    if w.left.color==0:
                        w.right.color=0
                        w.color=1
                        self.left_rotate(w)
                        w=x.parent.left
                    w.color=x.parent.color
                    x.parent.color=0
                    w.left.color=0
                    self.right_rotate(x.parent)
                    x=self.root
        x.color=0

    def insert(self,val):
        n=node(val)
        x=self.root
        y=self.nil
        while x!=self.nil:
            y=x
            x.size+=1
            if val<x.key:
                x=x.left
            else:
                x=x.right
        if y==self.nil:
            self.root=n
        elif val<y.key:
            y.left=n
        else:
            y.right=n
        n.parent=y
        n.left=self.nil
        n.right=self.nil
        n.color=1  # red
        self.insert_fixup(n)

    def delete(self,val):
        z=self.search(val)
        y=z
        y_original_color=y.color
        if z.right==self.nil:
            x=z.left  # x is the node moved to the place of y, when y is the node removed or moved within the tree.
                      # Color will only be wrong at x because y.color==z.color. So x needs to be fix up if y.color is
                      # black before

            i=z
            while i!=self.nil:
                i.size-=1
                i=i.parent
            self.nil.size=0

            self.transplant(z,z.left)
        elif z.left==self.nil:
            x=z.right

            i=z
            while i!=self.nil:
                i.size-=1
                i=i.parent
            self.nil.size=0

            self.transplant(z,z.right)
        else:
            y=self.min(z.right)  # equal to y=self.min(x.right)
            x=y.right

            i=z
            while i!=self.nil:
                i.size-=1
                i=i.parent
            self.nil.size=0

            y_original_color=y.color
            if y.parent==z:
                x.parent=y  # in case that x==self.nil
            else:
                self.transplant(y,y.right)
                z.right.parent=y
                y.right=z.right
            self.transplant(z,y)
            z.left.parent=y
            y.left=z.left
            y.color=z.color
        if y_original_color==0:
            self.delete_fixup(x)

    def delete_find_predecessor(self,val):
        z=self.search(val)
        y=z
        y_original_color=y.color
        if z.right==self.nil:
            x=z.left  # x is the node moved to the place of y, when y is the node removed or moved within the tree.
                      # Color will only be wrong at x because y.color==z.color. So x needs to be fix up if y.color is
                      # black before

            i=z.left
            while i!=self.nil:
                i=i.parent
                i.size-=1
            self.nil.size=0

            self.transplant(z,z.left)
        elif z.left==self.nil:
            x=z.right

            i=z.right
            while i!=self.nil:
                i=i.parent
                i.size-=1
            self.nil.size=0

            self.transplant(z,z.right)
        else:
            y=self.max(z.left)  # equal to y=self.min(x.right)
            x=y.left

            i=y
            while i!=self.nil:
                i=i.parent
                i.size-=1
            self.nil.size=0

            y_original_color=y.color
            if y.parent==z:
                x.parent=y  # in case that x==self.nil
            else:
                self.transplant(y,y.left)
                z.left.parent=y
                y.left=z.left
            self.transplant(z,y)
            z.right.parent=y
            y.right=z.right
            y.color=z.color
            y.size=y.left.size+y.right.size+1
        if y_original_color==0:
            self.delete_fixup(x)

    def rank(self,x):
        y=x.parent
        r=x.left.size+1
        while y!=self.nil:
            if y.right==x:
                r=r+y.left.size+1
            x=y
            y=x.parent
        return r

    def __select__(self,x,i):
        if i==x.left.size+1:
            return x
        elif i<x.left.size+1:
            return self.__select__(x.left,i)
        else:
            return self.__select__(x.right,i-x.left.size-1)

    def select(self,i):
        return self.__select__(self.root,i)

    def select_nonrecursive(self,i):
        r=self.root.left.size+1
        x=self.root
        while r!=i:
            if i<r:
                x=x.left
                r=x.left.size+1
            else:
                i=i-x.left.size-1
                x=x.right
                r=x.left.size+1
        return x

    def __key_rank__(self,k,r,x):  # r is the rank which should be inherited. the function is tail recursive
        if x==self.nil:
            print "cannot find key %d" %k
            return
        if x.key>k:
            return self.__key_rank__(k,r,x.left)
        elif x.key<k:
            return self.__key_rank__(k,r+x.left.size+1,x.right)
        else:
            return r+x.left.size+1

    def key_rank(self,k):
        return self.__key_rank__(k,0,self.root)

# test code
bst=RedBlackTree()

bst.insert(12)
bst.insert(5)
bst.insert(18)
bst.insert(2)
bst.insert(9)
bst.insert(15)
bst.insert(19)
bst.insert(13)
bst.insert(17)


bst.inorder_tree_walk_nonrecursive()   # 2 5 9 12 13 15 17 18 19


print bst.max(bst.root).key  # 19
print bst.min(bst.root).key  # 2
print bst.successor(bst.root).key # 13
print bst.successor(bst.root.left.right).key  # 12
print bst.predecessor(bst.root).key  # 9
print bst.predecessor(bst.root.right.left.left).key  # 12

'''
bst.delete_find_predecessor(12)  # delete 12

bst.delete_find_predecessor(15)  # delete 15

bst.delete(13)  # delete 13
'''

bst.inorder_tree_walk_nonrecursive()

print bst.rank(bst.root.left.right)

i=5
print bst.select(i).key

print bst.select_nonrecursive(i).key

print bst.key_rank(18)
