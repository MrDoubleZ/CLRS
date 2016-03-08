# Bubble Sort
def BubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1,i,-1):
            if (array[j]<array[j-1]):
                temp=array[j]
                array[j]=array[j-1]
                array[j-1]=temp


# test code for BubbleSort
array=[3,2,5,7,3,4,8,9,12,34,-1,-3,-99,0,0,2,3,77,13]
BubbleSort(array)
print array