def fib(n):
    a,b =1,1
    L1=[]
    for i in range(n-1):
        a,b = b,a+b
        L1.append(a)
    print L1 
print fib(6)
