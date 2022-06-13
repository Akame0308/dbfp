
from sys import byteorder


load = lambda x:[x[0:12].replace(b"\x00",b"").decode(),int.from_bytes(x[12:16],byteorder="little"),x[16:64].replace(b"\x00",b"").decode()]


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
        s = course.to_bytes(4,byteorder="little")
        f.write(s+index.to_bytes(4,byteorder="little"))

