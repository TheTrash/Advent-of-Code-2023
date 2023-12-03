f = open("input", "r")
l = [n for n in f.readlines()]


calibration = []
numbers = [ "1","2","3","4","5","6","7","8","9" ]
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]




def searcher(row):
    find_si, find_fi = (False,False)
    si = 0
    fi = len(row)-1
    tmp = [0,0]


    for i in range(fi):
        if row[i] in numbers:
            tmp[0] = i
            break
        
    for i in range(fi, -1, -1):
        if row[i] in numbers:
            tmp[1] = i
            break


    position = {}
    for di in digits:
        res = [i for i in range(len(row)) if row.startswith(di, i)]
        print(res)
        if res != []:
            for e in res:
                position[e] = di

    print(position)

    max_i, min_i = (0,1000)
    for di in position:
        if(di < min_i ):
            min_i = di
        if(di > max_i):
            max_i = di

    print(min_i, max_i)
    if(min_i < tmp[0]):
        tmp[0] = min_i
    if(max_i > tmp[1]):
        tmp[1] = max_i

    print(tmp)
    
    p = row[tmp[0]] if row[tmp[0]] in numbers else digits.index(position[tmp[0]])+1
    r = row[tmp[1]] if row[tmp[1]] in numbers else digits.index(position[tmp[1]])+1
    return int(p)*10 + int(r)


for row in l:
    calibration.append(searcher(row))

#print(calibration)

print(sum(calibration))