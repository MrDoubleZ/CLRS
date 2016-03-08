# Find-Maximum Subarray
def find(array,b,e):
    mid=(b+e)/2
    if (b==e):
        if (array[b]<0):
            return [0,mid,mid]
        else:
            return [array[b],b,e]
    else:
        [leftmaxsum,left_low,left_high]=find(array,b,mid)
        [rightmaxsum,right_low,right_high]=find(array,mid+1,e)
        [middlemaxsum,cross_low,cross_high]=findmiddle(array,b,e)
        if ((leftmaxsum>=rightmaxsum)and(leftmaxsum>=middlemaxsum)):
            return [leftmaxsum,left_low,left_high]
        elif (rightmaxsum>=leftmaxsum)and(rightmaxsum>=middlemaxsum):
            return [rightmaxsum,right_low,right_high]
        else:
            return [middlemaxsum,cross_low,cross_high]




def findmiddle(array,b,e):# in this function, array[mid] should always be put in the return list,
                        # no matter whether the return list is minimal

    mid=(b+e)/2
    leftsum=float('-inf')
    rightsum=float('-inf')

    sum=0
    for i in range(mid,b-1,-1):
        sum+=array[i]
        if sum>=leftsum:
            leftsum=sum
            low=i
    sum=0
    for i in range(mid+1,e+1):
        sum+=array[i]
        if sum>=rightsum:
            rightsum=sum
            high=i
    if leftsum+rightsum<0:
        return [0,mid,mid]
    else:
        return [leftsum+rightsum,low,high]



def FindMaxSubArray(array):
    return find(array,0,len(array)-1)
# test code
import time
array=[-13,-3,-25,-20,-3,-16,-23,-18,-20,-7,-12,-5,-22,-15,-4,-7]
start=time.clock()
print FindMaxSubArray(array)
end=time.clock()
print end-start