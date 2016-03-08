# find out the number of the inversions


global count
count=0

def merge(array,p,r,q):
    global count
    left=array[p:r+1]#p~r
    right=array[r+1:q+1]#r+1~q
    left.append(float('inf'))
    right.append(float('inf'))
    i=j=0
    for k in range(p,q+1):
        if (left[i]>right[j]):
            array[k]=right[j]
            j=j+1
            if (left[i]!=float('inf')):
                count+=r-p+1-i  # len(array)-i. when left[i]>right[j], left[i:end] are all bigger than right[j],
                                # since right[j] will pop at this time of loop, they cannot be counted at next loop.
                                # therefore it's necessary to count them at this loop.
        else:
            array[k]=left[i]
            i=i+1

def MergeSort(array,p,q):
    if (p<q):
        r=(p+q)/2#floor
        MergeSort(array,p,r)#p~r
        MergeSort(array,r+1,q)#r+1~q
        merge(array,p,r,q)


def FindInversion(array):
    MergeSort(array,0,len(array)-1)





# test code
array=[2,3,8,6,1,-1]#0~7
FindInversion(array)
print count
print array