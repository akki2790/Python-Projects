def cats():
    try:
        number = int(raw_input("How many cats do you have?"))
        if number>=4:
            print ("That is a lot of cats.")
        else:
            print ("Not that many cats")
    except:
        print ("you did not enter a int value")


cats()
