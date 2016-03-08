# development of insert sort, linear search->binary search
def Iter_BinarySearch(array,b,e,value):
    while(b<=e):#pay attention to the judgement!
        mid=(b+e)/2#floor
        if (array[mid]<value):#value in [mid,e]
            b=mid+1
        elif (array[mid]>value):#value in [b,mid]
            e=mid-1
        else:
            return mid
    return b

def InsertSort(array):
    for i in range(0, len(array)):
        key=array[i]
        index=Iter_BinarySearch(array,0,i-1,key)

        for k in range(i,index-1,-1):
            array[k]=array[k-1]

        array[index]=key


# test code
array=[15,14,13,11,12,9,10,5,4,2,3,1,8,7,0,6,-1,18]
InsertSort(array)
print array