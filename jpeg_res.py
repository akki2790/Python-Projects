def jpeg_res(filename):
    with open(filename, "rb") as img_file:
        img_file.seek(163)
        a=img_file.read(2)
        height = (a[0]<<8)+a[1]
        a=img_file.read(2)
        width = (a[0]<<8)+a[1]

    print ("the resolution of the picture is", width," x", height)
