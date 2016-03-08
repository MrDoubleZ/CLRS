# binary search

# iterative
def Iter_BinarySearch(array,b,e,value):
    while(b<=e):#pay attention to the judgement!
        mid=(b+e)/2#floor
        if (array[mid]<value):#value in [mid,e]
            b=mid+1
        elif (array[mid]>value):#value in [b,mid]
            e=mid-1
        else:
            print "find it! the index is: ", mid
            return mid
    print "cannot fint it!"
    return -1


# test code for iterative BinarySearch(array,b,e,value)
array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Iter_BinarySearch(array,0,15,15)


# recursive
def Recur_BinarySearch(arrray,b,e,value):
    mid=(b+e)/2#floor
    if (b<=e):
        if (array[mid]<value):#value in [mid,e]
            b=mid+1
        elif (array[mid]>value):#value in [b,mid]
            e=mid-1
        else:
            print "find it! the index is: ", mid
            return mid
    else:
        print "cannot find it"
        return
    Recur_BinarySearch(array,b,e,value)

# test code for recursive BinarySearch
array=[0, 1, 2, 3, 4, 5, 6, 7, 8,  9, 10, 11, 12, 13, 14, 15]
Iter_BinarySearch(array,0,15,16)