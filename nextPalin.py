def nextPalin(num):
    length=len(str(num))
    oddDighits=(length%2!=0)
    lefthalf=getlefthalf(num)
    middle=getmiddle(num)

    if oddDigits:
        increment=pow(10,length/2)
        newNum=int(lefthalf+middle+lefthalf[::-1])

    else:
        increment=int(1.1*pow(10, length/2))
        newNum=int(lefthalf+lefthalf[::-1])

    if newNum > num:
        return newNum

    if middle!='9':
        return newNum+increment

    else:
        return nextPalin(roundup(num))

def getlefthalf(num):
    return str(num)[:len(str(num))/2]

def getMiddle(num):
    return str(num)[(len(str(num))-1)/2]

def roundup(num):
    length=len(str(num))
    increment=pow(10,((length/2)+1))
    return ((num/increment)+1)*increment

