# Matrix Multiplication
def mul(A,B):
    m=len(A)
    n=len(A[0])
    _n=len(B)
    t=len(B[0])

    RES=[[0 for i in range(t)] for j in range(m)]
    #print RES

    if (_n!=n):
        print "error!"
        return -1
    for i in range(m+1):
        for j in range(n+1):
            print A[0][0]
    #for i in range(m+1):
    #    for j in range(t+1):
    #        for k in range(n+1):
    #            print [i,j,k]
    #            print A[i][n]*B[n][j]
    #            RES[i][j]+=A[i][n]*B[n][j]
    return RES



# test code
A=[[1,0],[0,1]]
B=[[1,2,3],[2,3,4]]
res=mul(A,B)
print res