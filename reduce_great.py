import functools

num = [1,2,3,4,5,6,78,2,3]

sum = functools.reduce(lambda x,y: x+y, num)
print sum


great = functools.reduce(lambda x,y: x if x>y else y, num)
print great
