file = open (".txt")

name_list=[]
for line in file:
    line=line.strip()
    name_list.append(line)

file.close()

key = "Some shit"

i = 0
while i < len(name_list) and name_list[i]!=key:
    i+=1

if i<len(name_list):
    print "The name is at the position ", i
else:
    print "The name is not in the list."


#***************


file = open("something.txt")

name_list1=[]
for line in file:
    line=line.strip()
    name_list.append(line)

file.close()

key = "some shit"

i=0
while i < len(name_list) and name_list[i]!=key:
    i+=1

if i<len(name_list1):
    print "the name is at the position", i
else:
    print "The name is not in the list."
