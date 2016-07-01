import random

def guesses():
    name = raw_input("What's your name?")
    p=["Well ", name, ", i want you to guess a number bet 1 and 20. you have 6 chances"]
    print ''.join(p)
    number = random.randint(1,20)

    for chance in range(6):
        guess = int(raw_input("guess a number: "))
        if (guess>number):
            print "Lower than that"
        elif (guess<number):
            print "Higher than that"
        else:
            print "That's it"
            break
    print "The number was", number

guesses()
