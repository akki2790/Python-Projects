l1 = ['a','b', 'c', 'd', 'e']
l2 = ['a', 'e', 'c', 'x']
l3 = ['f', 'g', 'k', 'y']
l4 = ['a', 'z', 't']

new = list(set().union(l1,l2,l3,l4))
print new
