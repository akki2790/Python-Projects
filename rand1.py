import random

def rand1(x,y):
    c=0
    L2=[]
    while c<=10:
        L2.append(random.randrange(x,y))
        c+=1
    return L2

print rand1(0,100)


def rand2(z,a):
    c=0
    L2=[]
    while c<=10:
        L2.append(random.randrange(z,a))
        c+=1
    return L2

print rand2(10,200)
