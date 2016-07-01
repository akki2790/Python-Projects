def long_words(lengths,n):
    for length in lengths:
        if length>n:
            print length

def longest_length(words):
    list_lengths=[]
    for word in words:
        list_lengths.append(len(word))
    print long_words(list_lengths,4)

longest_length(['akshay', 'mandlik', 'arun', 'sadhana'])


def long_words(words,n):
    for word in words:
        if len(word)>n:
            print len(word)

long_words(['akshay', 'mandlik', 'arun', 'sadhana'],4)
