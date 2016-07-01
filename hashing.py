import hashlib

def hash_file(filename):
    h=hashlib.sha1()
    #open the file and read it in a binary form
    with open(filename, "rb") as file:
        chunk = 0
        # while is to loop till the end of file
        while chunk != b"":
            chunk = file.read(1024)
            h.update(chunk)
    #return the hex representation of the digest
    return h.hexdigest()

message = hash_file("track1.mp3")
print message
