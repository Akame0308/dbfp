
load = lambda x:[x[0:12].replace(b"\x00",b"").decode(),x[12:16].replace(b"\x00",b"").decode(),x[16:64].replace(b"\x00",b"").decode()]


def generate():
    with open("data.dat","r+b") as f:
        block = f.read(64)
        index = 0
        while block != b'':
            #print(block,index)
            yield index,load(block)[1]
            block = f.read(64)
            index += 1

l = [i for i in generate()]
l.sort(key = lambda x:x[1])

with open("course.dat","wb") as f:
    for index,course in l:
        s = b"%4b"%(course.encode())
        f.write(s.replace(b"\x20",b"\x00")+index.to_bytes(4,byteorder="big"))

