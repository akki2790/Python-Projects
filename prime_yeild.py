def prime(n):
    if n==1:
        return False
    else:
        for x in range(2,n):
            if n%x==0:
                return False
    return True

def primes(n=1):
    while n<100:
        if prime(n): yield n
        n+=1

for n in primes():
    print n
