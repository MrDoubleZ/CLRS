#Linear search
array=[6,5,4,3,6,8,3,2,10,0,43,-2,-5]
search_val=3
for i in range(0,len(array)):
    if (search_val==array[i]):
        print "get! The index of value is: %d" %i