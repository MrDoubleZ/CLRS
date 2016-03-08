# -*- coding:utf-8 -*-

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







#test code

s1=Stack(3)
s1.isEmpty()
s1.pop()

s1.push(3)
s1.push(2)
s1.push(1)
s1.push(0)
print s1.pop()
print s1.pop()
print s1.pop()
print s1.pop()

