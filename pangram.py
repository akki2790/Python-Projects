def pangram(sentence):
    sentence=sentence.lower()
    list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    list2=[]
    for item in sentence:
        if item.isalpha():
            list2.append(item)
    for alph in list1:
        if alph not in list2:
            print 'false'
            return False
        else:
            print 'true'
            return True

pangram('The quick brown fox jumps over the lazy dog.')
