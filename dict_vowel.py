def dict_vowel():
    ip_str=raw_input("Enter a string: ")
    ip_str=ip_str.lower()
    count = {x:sum([1 for char in ip_str if char==x]) for x in "aeiou"}
    return count

print dict_vowel()

def dict_vowel1():
    ip_str = raw_input("Enter a string: ")
    ip_str = ip_str.lower()
    count = {x:sum([1 for char in ip_str if char==x]) for x in "aeiou"}
    return count

print dict_vowel1()
