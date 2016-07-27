


file = open("something.txt")

name_list1=[]
for line in file:
    name=line.split()
    name_list.append(name)

file.close()

key = "something"

i=0
while i < len(name_list) and name_list[i]!=key:
    i+=1

if i<len(name_list1):
    print "the name is at the position", i
else:
    print "The name is not in the list."
