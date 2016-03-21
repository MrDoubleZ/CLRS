# max-heap and heapsort


class Heap(object):
    def __init__(self,A):
        self.array=A
        self.heap_size=len(A)

    def parent(self,i):
        return (i-1)/2

    def left(self,i):
        return 2*i+1

    def right(self,i):
        return 2*i+2

    def max_heapify(self,i):
        l=self.left(i)
        r=self.right(i)
        if l<=self.heap_size-1 and self.array[l]>self.array[i]:
            largest=l
        else:
            largest=i
        if r<=self.heap_size-1 and self.array[r]>self.array[largest]:
            largest=r
        if largest!=i:
            temp=self.array[i]
            self.array[i]=self.array[largest]
            self.array[largest]=temp
            self.max_heapify(largest)

    def max_heapify_nonrecursive(self,i):
        while i<self.heap_size/2:
            l=self.left(i)
            r=self.right(i)
            if l<=self.heap_size-1 and self.array[l]>self.array[i]:
                largest=l
            else:
                largest=i
            if r<=self.heap_size-1 and self.array[r]>self.array[largest]:
                largest=r
            if largest!=i:
                temp=self.array[i]
                self.array[i]=self.array[largest]
                self.array[largest]=temp
                i=largest
            else:
                return

    def build_max_heap(self):
        self.heap_size=len(self.array)
        for i in range(self.heap_size/2-1,-1,-1):
            self.max_heapify(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self.array)-1,0,-1):
            temp=self.array[0]
            self.array[0]=self.array[i]
            self.array[i]=temp
            self.heap_size-=1
            #self.max_heapify(0)
            self.max_heapify_nonrecursive(0)

    def heap_maximum(self):
        return self.array[0]

    def heap_extract_max(self):
        if self.heap_size<0:
            print "heap underflow"
            return
        max=self.array[0]
        self.array[0]=self.array[self.heap_size-1]
        self.heap_size-=1
        #self.max_heapify(0)
        self.max_heapify_nonrecursive(0)
        return max

    def heap_increase_key(self,i,key):
        if key<self.array[i]:
            print "invalid key: it is smaller than current key"
            return
        self.array[i]=key
        p=self.parent(i)
        while self.array[p]<self.array[i] and i!=0:
            temp=self.array[p]
            self.array[p]=self.array[i]
            self.array[i]=temp
            i=p
            p=self.parent(i)

    def heap_insert(self,key):
        self.heap_size+=1
        self.array.append(-float('inf'))
        self.heap_increase_key(self.heap_size-1,key)

    def display(self):
        for i in range(len(self.array)):
            print array[i]

    def heap_delete(self,i):
        while i<self.heap_size/2-1:
            l=self.left(i)
            r=self.right(i)
            largest=l if self.array[l]>self.array[r] else r
            self.array[i]=self.array[largest]
            i=largest
        self.array[i]=self.array[self.heap_size-1]
        self.heap_size-=1


# test code

array=[2,4,7,9,3,8,16,14,1,10]
hp=Heap(array)
hp.display()

hp.build_max_heap()
print " "
hp.display()

'''
hp.heap_sort()
print " "
hp.display()
'''

'''
hp.heap_insert(18)
print " "
hp.display()

hp.heap_sort()
print " "
hp.display()
'''


hp.heap_delete(4)
print " "
hp.display()



