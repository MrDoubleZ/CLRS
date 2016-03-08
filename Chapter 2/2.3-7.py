# find 2 numbers from an array, sum of which is a given value exactly
def merge(array,p,r,q):
    left=array[p:r+1]#p~r
    right=array[r+1:q+1]#r+1~q
    i=j=0
    for k in range(p,q+1):
        if (i>=r-p+1):
            array[k]=right[j]
            j=j+1
        elif (j>=q-r):#not q-r+1, len(right)=q-(r+1)+1=q-r
            array[k]=left[i]
            i=i+1
        elif(left[i]>right[j]):
            array[k]=right[j]
            j=j+1
        elif(left[i]<=right[j]):
            array[k]=left[i]
            i=i+1


def merge_sort(array,b,e):
    mid=(b+e)/2
    if (e>b):
        merge_sort(array,b,mid)
        merge_sort(array,mid+1,e)
        merge(array,b,mid,e)


def MergeSort(array):
    merge_sort(array,0,len(array)-1)

def binary_search(array,b,e,value):
    while(b<=e):
        mid=(b+e)/2
        if(array[mid]>value):
            e=mid-1
        elif(array[mid]<value):
            b=mid+1
        else:
            return mid
    return -1

def BinarySearch(array,value):
    return binary_search(array,0,len(array)-1,value)


def FindValue(array,value):
    MergeSort(array)#O(nlgn)
    flag=0
    for k in range(len(array)):
        key=value-array[k]
        index=BinarySearch(array[k+1:len(array)],key)
        #print array[k+1:len(array)]
        if (index!=-1):
            print "find it! %d + %d = %d" % (array[k],array[index+k+1],value)
            flag=1
    if (flag==0):
        print "cannot find it!"






# test code for merge
array=[3,5,2,4,6,8,10]
merge(array,0,1,6)
print array

# test code for MergeSort
array=[3,2,5,7,1,4,8,9]#0~7
MergeSort(array)
print array

# test code for BinarySearch
array=[1, 2, 3, 4, 5, 7, 8, 9]#0~7
print BinarySearch(array,9)

# test code for FindValue
array=[3,2,5,7,1,4,8,9]#0~7
FindValue(array,12)