def char_freq(shitz):
    noshit=[]
    for shit in shitz:
        if shit not in noshit:
            noshit.append(shit)
    print noshit
    return noshit

char_freq('abbabcbdbabdbdbabababcbcbab')
