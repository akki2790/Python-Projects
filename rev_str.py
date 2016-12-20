def rev_str(s):
    s=list(s)
    rev=[]
    while len(s)>0:
        rev.append(s.pop())
    return ''.join(rev)


print rev_str("akshay")



def rev_str1():
    rev=[]
    string=raw_input("Whats the word?: ")
    string=list(string)
    x=len(string)
    while x!=0:
        rev.append(string[x-1])
        x-=1
    rev=''.join(rev)
    print rev

rev_str1()
