import os

#debug = print
debug = lambda *x:None

def get_datas_by_index(indexes):
    with open("data.dat","r+b") as f:
        load_ind = lambda x:[x[0:12].replace(b"\x00",b"").decode(),x[12:16].replace(b"\x00",b"").decode(),x[16:64].replace(b"\x00",b"").decode()]
        res = []
        for index in indexes:
            f.seek(index*64)
            data = f.read(64)
            res.append(load_ind(data))
    return res

def get_by_student_id(index):
    load_stu = lambda x:[x[0:12].replace(b"\x00",b"").decode(),int.from_bytes(x[12:16],byteorder="big")]
    with open("student.dat","r+b") as file:
        file.seek(index*16)
        data = file.read(16)
    debug(load_stu(data))
    return load_stu(data)

def search_by_student_id(student_id):
    
    filename = "student.dat"
    limit = os.path.getsize(filename)//16
    left = 0
    right = limit-1
    debug(student_id,get_by_student_id(left)[0],get_by_student_id(right)[0])
    debug(student_id < get_by_student_id(left)[0],student_id > get_by_student_id(right)[0])
    if student_id < get_by_student_id(left)[0] or student_id > get_by_student_id(right)[0]:
        return []
    
    while right - left > 5:
        mid = (right+left) // 2
        d = get_by_student_id(mid)
        if d[0] < student_id:
            left = mid
        else:
            right = mid
    
    res = []

    while left < limit:
        d = get_by_student_id(left)
        if d[0] < student_id:
            left += 1
            continue
        if d[0] > student_id:
            break

        res.append(d[1])
        left += 1
    
    return res
    

def get_by_course_id(index):
    load_cou = lambda x:[x[0:4].replace(b"\x00",b"").decode(),int.from_bytes(x[4:8],byteorder="big")]
    with open("course.dat","r+b") as file:
        file.seek(index*8)
        data = file.read(8)
    return load_cou(data)

def search_by_course_id(course_id):
    
    filename = "course.dat"
    limit = os.path.getsize(filename)//8
    left = 0
    right = limit-1
    debug(course_id,get_by_course_id(left)[0],get_by_course_id(right)[0])
    debug(course_id < get_by_course_id(left)[0],course_id > get_by_course_id(right)[0])
    if course_id < get_by_course_id(left)[0] or course_id > get_by_course_id(right)[0]:
        return []
    
    while right - left > 5:
        mid = (right+left) // 2
        d = get_by_course_id(mid)
        if d[0] < course_id:
            left = mid
        else:
            right = mid
    
    res = []

    while left < limit:
        d = get_by_course_id(left)
        if d[0] < course_id:
            left += 1
            continue
        if d[0] > course_id:
            break

        res.append(d[1])
        left += 1
    
    return res
    



while True:
    l = input().split()
    if not l:
        continue

    if l[0] == "Exit":
        break
    
    elif l[0].lower() in ("s","student","student_id"):
        res = search_by_student_id(l[1])
        res = get_datas_by_index(res)
        res.sort(key=lambda x:x[1])
        print("\n".join(map(lambda x:" ".join(x),res)))
    elif l[0].lower() in ("c","course"):
        res = search_by_course_id(l[1])
        res = get_datas_by_index(res)
        res.sort(key=lambda x:x[1])
        print("\n".join(map(lambda x:" ".join(x),res)))