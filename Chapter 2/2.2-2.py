#Selection Sort
array=[6,5,4,3,6,8,3,2,10,0,43,-2,-5]


for j in range(0,len(array)):
    min_index=j
    for i in range(j+1,len(array)):
        if(array[i]<array[min_index]):
            min_index=i
    temp=array[j]
    array[j]=array[min_index]
    array[min_index]=temp
print array