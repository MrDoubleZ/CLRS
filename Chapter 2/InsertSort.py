#Insert Sort nondecreasing order
array=[6,5,4,3,6,8,3,2,1]
for i in range(0, len(array)):
    key=array[i]
    j=i-1
    while((j>-1)and(key<array[j])):#pay attention to judgement j>-1
        array[j+1]=array[j]
        j=j-1
    array[j+1]=key
print array