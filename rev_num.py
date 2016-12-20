def rev_num(n):
    rev=[]
    while n>0:
        rev.append(str(n%10))
        n/=10
    return int(''.join(rev))

print rev_num(12345)



def rev_num1():
    number=int(raw_input("whats the numnber??: "))
    rev=[]
    while number!=0:
        x=str(number%10)
        rev.append(x)
        number=number/10
    rev1=''.join(rev)
    print rev1

rev_num1()
