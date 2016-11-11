def factorial(num):
        factorial = 1
        if num<0:
            return False
        elif num==0:
            print "factorial of 0 is 1"
            return False
        else:
            for i in range(1, num+1):
                factorial = factorial*i
            print "The factorial is ", factorial
            return True
        
factorial(5)
            
                
