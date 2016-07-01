import random

def list2(x,y):
    c=0
    L2=[]
    while c<=10:
        L2.append(random.randrange(x,y))
        c+=1
    print L2

list2(0,100)
    
