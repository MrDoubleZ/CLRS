#Merge Sort without sentinel
def merge(array,p,r,q):
    left=array[p:r+1]#p~r
    right=array[r+1:q+1]#r+1~q
    print "left:",left
    print "right:",right
    i=j=0
    for k in range(p,q+1):
        if (i==len(left)):
            for ii in range(k,k+len(right)-j):
                array[ii]=right[j]
                j=j+1
            return
        if (j==len(right)):
            for jj in range(k,k+len(left)-i):
                array[jj]=left[i]
                i=i+1
            return
        if (left[i]>right[j]):
            array[k]=right[j]
            j=j+1
        else:
            array[k]=left[i]
            i=i+1

def MergeSort(array,p,q):
    if (p<q):
        r=(p+q)/2#floor
        MergeSort(array,p,r)#p~r
        MergeSort(array,r+1,q)#r+1~q
        merge(array,p,r,q)

#test code:
array=[3,2,5,7,3,4,8,9]#0~7
MergeSort(array,0,7)
print array