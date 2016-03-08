# single linked list with sentinel

class node(object):
    def __init__(self,val):
        self.value=val
        self.next=None

class SingleLinkedList(object):
    def __init__(self):
        self.sentinel=node(None)
        self.sentinel.next=self.sentinel
        self.head=self.sentinel

    def insert(self,val):
        n=node(val)
        n.next=self.sentinel.next
        self.sentinel.next=n

    def search(self,val):# if val node exists, return node, otherwise, return -1
        x=self.head.next
        while (x!=self.sentinel)and(x.value!=val):
            x=x.next
        if x==self.sentinel:
            print "cannot find the value"
            return False
        else:
            return x

    def delete(self,val):
        x=self.head.next
        prev=self.head
        while (x!=self.sentinel)and(x.value!=val):
            prev=x
            x=x.next
        if x==self.sentinel:
            print "cannot find the value"
            return False
        else:
            prev.next=x.next
            print "delete the node of %d" %val

    def display(self):
        x=self.head.next
        while x!=self.sentinel:
            print x.value
            x=x.next

    def reverse(self):
        x_prev=self.head
        x_curr=x_prev.next
        x_next=x_curr.next

        while x_curr!=self.sentinel:
            x_curr.next=x_prev

            x_prev=x_curr
            x_curr=x_next
            x_next=x_next.next

        self.sentinel.next=x_prev
        self.head=self.sentinel

# test code
sll=SingleLinkedList()
sll.delete(2)# cannot find the value
sll.delete(3)# cannot find the value
sll.search(1)# cannot find the value
sll.insert(1)
sll.insert(3)
sll.insert(8)
sll.search(1)
sll.search(8)
sll.search(3)
sll.delete(8)# delete the node of 8
sll.search(8)# cannot find the value
sll.delete(9)# cannot find the value


sll.display()

sll.insert(5)
sll.insert(7)
sll.insert(9)
sll.insert(11)
sll.insert(13)
sll.insert(15)

sll.display()

sll.reverse()
print "after reversing"
sll.display()