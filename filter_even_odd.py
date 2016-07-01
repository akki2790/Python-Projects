numbers = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,18]

odd = list(filter(lambda x:x%2, numbers))
print odd

even = list(filter(lambda x:x%2==0, numbers))
print even

# always remember... "filter(func,seq)"
