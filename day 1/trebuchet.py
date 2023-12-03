f = open("input", "r")
l = [n for n in f.readlines()]


calibration = []
numbers = [ "1","2","3","4","5","6","7","8","9" ]

def searcher(row):
    
    find_si, find_fi = (False,False)
    si = 0
    fi = len(row)-1
    tmp = [0,0]
    for i in range(fi):
        if row[i] in numbers:
            tmp[0] = int(row[i])
            break
    
    for i in range(fi, -1, -1):
        if row[i] in numbers:
            tmp[1] = int(row[i])
            break

    print(row, tmp)
    return (tmp[0]*10 + tmp[1])

print(searcher(l[0]))


for row in l:
    calibration.append(searcher(row))

#print(calibration)

print(sum(calibration))