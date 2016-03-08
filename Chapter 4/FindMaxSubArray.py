# Find-Maximum Subarray
def find(array,b,e):
    mid=(b+e)/2
    if (b==e):
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
    '''
    mid=(b+e)/2
    #print b,e,mid,range(mid-1,b-1,-1)
    sum=array[mid]+array[mid+1]
    index_left=mid
    index_right=mid+1
    for i in range(mid-1,b-1,-1):
        #print "in for loop1"
        if(sum+array[i]) >= sum:# error code! ALL sum of subarray should be traversed!
            sum+=array[i]
            index_left=i
    for i in range(mid+2,e+1):
        #print "in for loop2"
        if((sum+array[i])>=sum):
            sum+=array[i]
            index_right=i
    return [sum,index_left,index_right]
    '''
    mid=(b+e)/2
    leftsum=float('-inf')
    rightsum=float('-inf')

    sum=0
    for i in range(mid,b-1,-1):# mid-1 is incorrent because minimal index is 0
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
    return [leftsum+rightsum,low,high]



def FindMaxSubArray(array):
    return find(array,0,len(array)-1)
# test code
array=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]

print FindMaxSubArray(array)

