# a nonrecursive linear-time algorithm for the maximum subarray problem
# -*- coding:utf-8 -*-
class subarray(object):
    def __iter__(self):
        self.low=0
        self.high=0
        self.sum=0


def find(array):
    # init
    #s=[subarray()]*len(array)
    s=[]
    for i in range(len(array)):
        s.append(subarray())
    s[0].sum=array[0]
    s[0].low=0
    s[0].high=0
    for i in range(1,len(array)):
        s[i].low=s[i].high=0
        s[i].sum=0


    for i in range(len(s)):
        print [s[i].low,s[i].high,s[i].sum]

    # 寻找结尾为j的最大子串，并将结果存放于s中，再遍历s，找出这些子串中最大的那一个
    # 基于事实：max subarray一定会以某个下标j结尾，所以先列出每一个以j结尾的最大子串(j=[0,15])
    for i in range(1,len(array)):
        if s[i-1].sum<0:
            s[i].low=i
            s[i].high=i
            s[i].sum=array[i]
        else:
            s[i].low=s[i-1].low
            s[i].high=i
            s[i].sum=array[i]+s[i-1].sum
    for i in range(len(s)):
        print [s[i].low,s[i].high,s[i].sum]


    maxarray=subarray()
    maxarray.sum=s[0].sum
    maxarray.low=maxarray.high=0
    print "maxarray_init: ",[maxarray.low,maxarray.high,maxarray.sum]
    for i in range(len(s)):
        print [s[i].low,s[i].high,s[i].sum]
        if s[i].sum>maxarray.sum:
            print "change"
            maxarray=s[i]

    return maxarray

# test code
array=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
max=find(array)
print [max.low,max.high,max.sum]

