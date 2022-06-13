
with open("origin_data.csv","r") as f:
    data = f.read()

data = data.split("\n")[1:-1]
data = list(map(lambda x:x.split(","),data))
#data.sort(key=tuple)

with open("output.dat","wb") as f:
    for d in data:
        line = b"%-12b%-4b%-48b"%(d[0].encode(),int(d[1]).to_bytes(4,byteorder="little"),d[2].encode())
        line = line.replace(b"\x20",b"\x00")
        l = f.write(line)