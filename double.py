def double(array):
    checklist=[]
    for a in array:
        if a not in checklist:
            checklist.append(a)
        else:
            print a+" double hai bhai"
            return True

double("abhsjeufbskncvleyhdks")


def double1(array1):
    checklist1=[]
    for a in array1:
        a=a.lower()
        if a not in checklist1:
            checklist1.append(a)
            print "".join(checklist1)
        else:
            print a+" double hai bhai"
            return True

double1("sdbJKSBUIBKLSJDbvusbKCV DS")
