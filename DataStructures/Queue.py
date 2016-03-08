# -*- coding:utf-8 -*-

#Queue

class Queue(object):
    def __init__(self,len):
        self.array=[0 for i in range(len)]
        self.max_length=len
        self.head=0
        self.tail=0

    def enqueue(self,value):
        if self.head==(self.tail+1)%self.max_length:#queue is full
            print "overflow"
            return
        else:
            self.array[self.tail]=value
            self.tail=(self.tail+1)%self.max_length

    def dequeue(self):
        if self.tail==self.head:
            print "underflow"
            return
        else:
            self.head=(self.head+1)%self.max_length
            return self.array[self.head-1]


#test code
q1=Queue(5)
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

