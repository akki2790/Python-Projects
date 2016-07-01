def shortest_pal(word):
    if list(word)==list(reversed(word)):
        print "its my pal"
    else:
        print "not a pal"

shortest_pal("aabrarbaa")


#*************

def pal(word):
    if list(word)==list(reversed(word)):
        print "its my pal"
    else:
        print "nat a pal"

pal('palap')
