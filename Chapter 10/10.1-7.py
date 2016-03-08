# implement a stack with two queues

class Queue(object):
    def __init__(self,len):
        self.array=[0 for i in range(len)]
        self.max_length=len
        self.head=0
        self.tail=0

    def enqueue(self,value):
        if self.head==(self.tail+1)%self.max_length:#queue is full
            print "queue is overflow"
        else:
            self.array[self.tail]=value
            self.tail=(self.tail+1)%self.max_length

    def dequeue(self):
        if self.tail==self.head:
            print "queue is underflow"
            return
        else:
            self.head=(self.head+1)%self.max_length
            return self.array[self.head-1]

    def is_left_one(self):
        if (self.tail-self.head)%self.max_length==1:
            return True
        else:
            return False

    def is_empty(self):
        if self.tail==self.head:
            return True
        else:
            return False


class StackUsingQueue(object):
    def __init__(self,len):
        self.q1=Queue(len)
        self.q2=Queue(len)

    def is_empty(self):
        if self.q1.is_empty() and self.q2.is_empty():
            return True
        else:
            return False

    def push(self,val):
        if not self.q1.is_empty():
            self.q1.enqueue(val)
        else:
            self.q2.enqueue(val)

    def pop(self):
        if self.q1.is_empty():
            if not self.q2.is_empty():
                # q2->q1
                while not(self.q2.is_left_one()):
                    self.q1.enqueue(self.q2.dequeue())
                return self.q2.dequeue()
            else:
                print "stack_using_queue is underflow"
        else:
            # q1->q2
            while not(self.q1.is_left_one()):
                self.q2.enqueue(self.q1.dequeue())
            return self.q1.dequeue()


#test code

s1=StackUsingQueue(5)  # stack's capacity is n-1

print s1.is_empty()

s1.pop()

s1.push(3)
s1.push(2)
s1.push(1)
s1.push(0)
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()
