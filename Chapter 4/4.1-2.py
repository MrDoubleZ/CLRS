# brute-force method of solving maximum-subarray problem
def FindMaxSubArray(array):
    maxsum=array[0]
    low=high=0
    for i in range(len(array)):
        sum=array[i]
        for j in range(i+1,len(array)):
            sum+=array[j]
            if sum>=maxsum:
                maxsum=sum
                low=i
                high=j
    return [maxsum,low,high]

# test code
import time
array=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
start=time.clock()
print FindMaxSubArray(array)
end=time.clock()
print end-start