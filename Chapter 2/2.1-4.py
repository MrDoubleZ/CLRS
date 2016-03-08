a=[1,0,1,1, 1,1,0,1]
b=[1,0,0,0, 0,1,1,0]

ans=[0 for i in range(len(a)+1)]
carry=0
for i in range(len(a)):
    ans[i]=(a[i]+b[i]+carry)%2
    carry=(a[i]+b[i]+carry)/2
ans[i+1]=carry
print ans