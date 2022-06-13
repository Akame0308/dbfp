import os



def get(file,index):
    load = lambda x:[x[0:12].decode().strip(),x[12:16].decode().strip(),x[16:64].decode().strip()]
    file.seek(index*64)
    data = file.read(64)
    return load(data)

def binary_search(student_id):
    
    filename = "data.dat"
    f = open(filename,"r+b")
    limit = os.path.getsize(filename)//64
    left = 0
    right = limit-1
    
    if student_id < get(f,left)[0] or student_id > get(f,right)[0]:
        return []
    
    while right - left > 5:
        mid = (right+left) // 2
        d = get(f,mid)
        if d[0] < student_id:
            left = mid
        else:
            right = mid
    
    res = []

    while left < limit:
        d = get(f,left)
        if d[0] < student_id:
            left += 1
            continue
        if d[0] > student_id:
            break

        res.append(d)
        left += 1
    
    return res
    



while True:
    l = input()
    if l == "Exit":
        break

    res = binary_search(l)
    res.sort(key = lambda x:x[1])
    print("\n".join(map(lambda x:" ".join(x),res)))