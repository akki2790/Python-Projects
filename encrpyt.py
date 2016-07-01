def encry():
    text = raw_input("enter the text to be encrypted: ")
    encrypted = ""
    for c in text:
        x=ord(c)
        x=x+1
        c2=chr(x)
        encrpyted = encrypted+c2
    return (encrypted)

print encry()


