# quick sort
import random
class QuickSort(object):
    def __init__(self,ary):
        self.array=ary

    def display(self):
        for i in self.array:
            print i,
        print

    def parition(self,p,r):
        x=self.array[r]
        i=p-1;
        for j in range(p,r): #  [p,r)
            if self.array[j]<=x:
                i+=1
                temp=self.array[i]
                self.array[i]=self.array[j]
                self.array[j]=temp
        temp=self.array[i+1]
        self.array[i+1]=self.array[r]
        self.array[r]=temp
        return i+1

    def random_parition(self,p,r):
        i=random.randint(p,r)
        x=self.array[i]
        self.array[i]=self.array[r]
        self.array[r]=x
        return self.parition(p,r)

    def __quick_sort__(self,p,r):
        if p<r:
            q=self.random_parition(p,r)
            self.__quick_sort__(p,q-1)
            self.__quick_sort__(q+1,r)

    def quick_sort(self):
        self.__quick_sort__(0,len(self.array)-1)

    def hoare_parition(self,p,r):
        i=p-1
        j=r+1
        x=self.array[p]
        while(True):
            while(True):
                i+=1
                if self.array[i]>=x or i==r:
                    break
            while(True):
                j-=1
                if self.array[j]<=x or j==p:
                    break
            if i<j:
                temp=self.array[i]
                self.array[i]=self.array[j]
                self.array[j]=temp
            else:
                return j

    def __hoare_quicksort__(self,p,r):
        if p<r:
            q=self.hoare_parition(p,r)
            self.__hoare_quicksort__(p,q)
            self.__hoare_quicksort__(q+1,r)

    def hoare_quicksort(self):
        self.__hoare_quicksort__(0,len(self.array)-1)

    def parition_3section(self,p,r):
        x=self.array[r]
        i=p-1;
        for j in range(p,r): #  [p,r)
            if self.array[j]<x:
                i+=1
                temp=self.array[i]
                self.array[i]=self.array[j]
                self.array[j]=temp
        temp=self.array[i+1]
        self.array[i+1]=self.array[r]
        self.array[r]=temp
        i=i+1
        res1=i
        for j in range(i+1,r+1):
            if self.array[j]==x:
                i+=1
                temp=self.array[i]
                self.array[i]=self.array[j]
                self.array[j]=temp
        res2=i
        return [res1,res2]

    def random_parition_3section(self,p,r):
        i=random.randint(p,r)
        x=self.array[i]
        self.array[i]=self.array[r]
        self.array[r]=x
        return self.parition_3section(p,r)

    def __quicksort_3section__(self,p,r):
        if p<r:
            [q,t]=self.parition_3section(p,r)
            self.__quicksort_3section__(p,q-1)
            self.__quicksort_3section__(t+1,r)

    def quicksort_3section(self):
        self.__quicksort_3section__(0,len(self.array)-1)


# test code
array=[2,7,5,3,1,4,9,10,12,55,32,21,1,2,3,3,3,3,3]
'''
rhm=QuickSort(array)
rhm.quick_sort()
rhm.display()
'''
rhm=QuickSort(array)
rhm.quicksort_3section()
rhm.display()



