def rev_num():
    number=int(raw_input("whats the numnber??: "))
    rev=[]
    while number!=0:
        x=str(number%10)
        rev.append(x)
        number=number/10
    rev1=''.join(rev)
    print rev1

rev_num()
