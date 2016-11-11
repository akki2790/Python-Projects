def double(array):
    checklist=[]
    for a in array:
        if a not in checklist:
            checklist.append(a)
        else:
            print a+" double hai bhai"
            return True

double("abhsjeufbskncvleyhdks")
