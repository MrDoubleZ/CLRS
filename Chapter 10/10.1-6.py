# implement a queue with two stacks
class Stack(object):
    def __init__(self,len):
        self.stack_array=[None for i in range(len)]
        self.max_length=len
        self.current_length=0
    def push(self,value):
        if self.current_length==self.max_length:
            print "stack overflow"
            return False
        else:
            self.current_length+=1
            self.stack_array[self.current_length-1]=value
            return True

    def pop(self):
        if self.current_length==0:
            print "stack underflow"
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

class Queue_usingstack(object):
    def __init__(self,len):
        self.s1=Stack(len)
        self.s2=Stack(len)

    def enqueue(self,val):
        if self.s1.isEmpty():
            # s2->s1
            while not(self.s2.isEmpty()):
                self.s1.push(self.s2.pop())
            self.s1.push(val)
        else:
            self.s1.push(val)

    def dequeue(self):
        if self.s2.isEmpty():
            # s1->s2
            while not(self.s1.isEmpty()):
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()
# test code
q1=Queue_usingstack(5)
q1.dequeue()#the queue is empty
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)#the queue is full, the capacity of queuq which length is n is n-1
q1.enqueue(1)#the queue is full
print q1.dequeue()
print q1.dequeue()
print q1.dequeue()
print q1.dequeue()
print q1.dequeue()#the queue is empty
print q1.dequeue()#the queue is empty