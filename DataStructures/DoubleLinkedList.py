# double linked list with sentinel

class node(object):
    def __init__(self,val):
        self.value=val
        self.prev=None
        self.next=None




class DoubleLinkedList(object):
    def __init__(self):
        self.sentinel=node(0)
        self.sentinel.prev=self.sentinel
        self.sentinel.next=self.sentinel


    def insert(self,n):
        n.next=self.sentinel.next
        n.prev=self.sentinel
        self.sentinel.next.prev=n
        self.sentinel.next=n


    def search(self,val):
        x=self.sentinel.next
        while (x!=self.sentinel)and(x.value!=val):
            x=x.next
        return x

    def delete(self,n):
        if self.sentinel.next==self.sentinel:
            print "linked list is empty"
            return
        else:
            n.prev.next=n.next
            n.next.prev=n.prev

# test code

ll=DoubleLinkedList()
n=node(1)
ll.insert(n)
ll.delete(n)
ll.delete(n)
n1=node(1)
n2=node(2)
n3=node(3)
ll.insert(n1)
ll.insert(n2)
ll.insert(n3)
print ll.search(4).value



