#Double ended queue, write 4 O(1)-time procedures to insert and delete the element at both sides of the deque

class Deque(object):
    def __init__(self,len):
        self.array=[0 for i in range(len)]
        self.max_length=len
        self.lhead=0
        self.rhead=1

    def leftEnqueue(self,value):
        if self.rhead==(self.lhead-1)%self.max_length:
            print "overflow"
            return
        else:
            self.array[self.lhead]=value
            self.lhead=(self.lhead-1)%self.max_length

    def leftDequeue(self):
        if self.rhead==(self.lhead+1)%self.max_length:
            print "underflow"
            return
        else:
            self.lhead=(self.lhead+1)%self.max_length
            return self.array[(self.lhead)%self.max_length]

    def rightEnqueue(self,value):
        if self.lhead==(self.rhead+1)%self.max_length:
            print "overflow"
            return
        else:
            self.array[self.rhead]=value
            self.rhead=(self.rhead+1)%self.max_length

    def rightDequeue(self):
        if self.lhead==(self.rhead-1)%self.max_length:
            print "underflow"
            return
        else:
            self.rhead=(self.rhead-1)%self.max_length
            return self.array[(self.rhead)%self.max_length]


#test code
d1=Deque(7)
d1.leftDequeue()#underflow
d1.rightDequeue()#underflow

d1.leftEnqueue(1)
d1.leftEnqueue(2)
d1.leftEnqueue(3)
d1.leftEnqueue(4)
d1.leftEnqueue(5)
d1.leftEnqueue(6)#overflow
print d1.leftDequeue()#5
d1.rightEnqueue(5)
d1.rightEnqueue(6)#overflow

print d1.rightDequeue()#5
print d1.rightDequeue()#1
print d1.rightDequeue()#2
print d1.rightDequeue()#3
print d1.rightDequeue()#4

d1.rightDequeue()#underflow