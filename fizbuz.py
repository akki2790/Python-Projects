def fizzbuzz(ranger):
    for number in range(1,ranger):
        if number%3==0:
            print "Fizz"
        elif number%5==0:
            print "Buzz"
        else:
            print number

fizzbuzz(100)
