def rev_str():
    rev=[]
    string=raw_input("Whats the word?: ")
    string=list(string)
    x=len(string)
    while x!=0:
        rev.append(string[x-1])
        x-=1
    rev=''.join(rev)
    print rev

rev_str()
