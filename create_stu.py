
load = lambda x:[x[0:12].replace(b"\x00",b"").decode(),int.from_bytes(x[12:16],byteorder="little"),x[16:64].replace(b"\x00",b"").decode()]


def generate():
    with open("data.dat","r+b") as f:
        block = f.read(64)
        index = 0
        while block != b'':
            #print(block,index)
            yield index,load(block)[0]
            block = f.read(64)
            index += 1

l = [i for i in generate()]
l.sort(key = lambda x:x[1])

with open("student.dat","wb") as f:
    for index,student_id in l:
        s = b"%12b"%(student_id.encode())
        f.write(s.replace(b"\x20",b"\x00")+index.to_bytes(4,byteorder="little"))

