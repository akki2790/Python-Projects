
import itertools,random



deck = list(itertools.product(range(0,12),['spade','club','daimond','heart']))

random.shuffle(deck)

for i in range(5):
    print 'you got', deck[i][0], 'of', deck[i][1]


                                           
