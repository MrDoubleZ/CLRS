#Find max subarray
array=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
low=0
high=0
sum=array[0]
tempsum=0
for i in range(len(array)):
    tempsum=max(array[i],tempsum+array[i])
    if tempsum>sum:
        high=i
        sum=tempsum
    if tempsum==array[i]:
        low=i

print [sum,low,high]