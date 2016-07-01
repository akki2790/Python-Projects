import hashlib

def hash(filename):
    h=hashlib.sha1()
    with open(filename,"rb") as file:
        chunk = 0
        while chunk != b"":
            chunk=file.read(1024)
            h.update(chunk)

    return h.hexdigest()

message = hash_file("track.mp3")
print message



import hashlib

def hash(filename):
    h=hashlib.sha1()
    with open(filename,"rb") as file:
        chunk = 0
        while chunk!=b"":
            chunk=file.read(1024)
            h.update(chunk)
    return h.hexdigest()

message = hash("track.mp3")
print message
