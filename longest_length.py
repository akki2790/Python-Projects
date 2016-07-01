def maxi(lengths):
    x=0
    for length in lengths:
        if length>x:
            x=length
    return x

def longest_length(words):
    list_lengths=[]
    for word in words:
        list_lengths.append(len(word))
    print maxi(list_lengths)

longest_length(['akshay', 'mandlik', 'arun', 'sadhana'])

##########################

def longest_word(words):
    x=0
    for word in words:
        if len(word)> x:
            x=len(word)
    return x

print longest_word(['akshay', 'mandlik', 'arun', 'sadhana'])
