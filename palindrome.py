def palindrome(sentence):
    sentence=sentence.lower()
    list1 = []
    for item in sentence:
        if item.isalpha():
            list1.append(item)
    print list1
    if list1==list1[::-1]:
        print "true"
        return True
    else:
        print "false"
        return False

palindrome("Was it a rat I saw")

def pal(sentence):
    sentence = ''.join(sentence.split()).lower()
    # or sentence = sentence.replace(" ","").lower()
    if list(sentence)==list(reversed(sentence)):
        print "true"
        return True
    else:
        print "false"
        return False

pal ("Was it a rat I saw")
