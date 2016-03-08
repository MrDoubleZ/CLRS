# Insert Sort
def insert(array,b,e):
    i=e-1
    key=array[e]
    while(i!=-1)and(key<array[i]):
        array[i+1]=array[i]
        i=i-1
    array[i+1]=key


def InsertSort(array,b,e):
    if (b<e-1):
        InsertSort(array,b,e-1)
    insert(array,b,e)


# test code for insert(array,b,e)
a=[2,3,4,5,6,1]
insert(a,0,5)
print a

# test code for InsertSort(array,b,e)
array=[15,14,13,11,12,9,10,5,4,2,3,1,8,7,0,6]
InsertSort(array,0,15)
print array