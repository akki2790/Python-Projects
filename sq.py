terms = int(raw_input('how many terms?'))

result = list(map(lambda x: 2 ** x, range(terms)))

print result

for i in range(terms):
    print '2 raised to', i , 'is', result[i]


#*******
    
terms = int(raw_input("How many terms?:" ))

result = list(map(lambda x: 2**x, range(terms)))

for i in range(terms):
    print "2 raised to", i ,"is ", result[i]
    
