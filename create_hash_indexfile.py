from collections import defaultdict
import enum
bucket = 709

inf = open("origin_data.csv","r")

d = inf.read().split("\n")[1:-1]

inf.close()
outf = open("index_file.dat","wb+")

dic = defaultdict(list)

for i,id in enumerate(map(lambda x:x.split(",")[0].replace("D","68"),d)):
    dic[int(id)%bucket].append([i,id])


outf.write(bucket.to_bytes(4,byteorder="little"))
outf.seek(4*(bucket+2))
for i in range(bucket):
    cur = outf.tell()
    outf.seek((i+1)*4)
    outf.write(cur.to_bytes(4,byteorder="little"))
    outf.seek(cur)

    for l in dic[i]:
        outf.write(int(l[1]).to_bytes(8,byteorder="little"))
        outf.write(l[0].to_bytes(8,byteorder="little"))

cur = outf.tell()
outf.seek((bucket+1)*4)
outf.write(cur.to_bytes(4,byteorder="little"))
outf.close()
