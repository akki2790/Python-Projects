def vowel_count():
    vowels="aeiou"
    ip_str = raw_input("Enter a string: ")
    ip_str = ip_str.lower()
    count={}.fromkeys(vowels,0)

    for char in ip_str:
        if char in count:
            count[char]+=1

    return count

print vowel_count()


def vowel_count():
    vowels = 'aeiou'
    ip_str = raw_input("Enter a string:")
    ip_str = ip_str.lower()
    count = {}.fromkeys(vowels,0)

    for char in ip_str:
        if char in count:
            count[char]+=1

    return count

print vowel_count()
