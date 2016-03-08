# print Fibonacci numbers
def Fibonacci(n):
    if (n>=3):
        return Fibonacci(n-1)+Fibonacci(n-2) # if using tail recursive, it will need less memory
    else:
        return 1

# test code
print Fibonacci(6)

for i in range(20):
    print Fibonacci(i)