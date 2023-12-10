f = open("input", "r")
l = [ n.replace("\n", "").split(" ") for n in f.readlines()]


res = []
for curr in range(len(l)):

    passage = [l[curr][::-1]]
    p = 0
    while(True):
        passage.append([])
        for i in range((len(passage[p])-1)):
            #print(int(passage[p][i]), int(passage[p][i+1]))
            passage[p+1].append((int(passage[p][i+1]) - int(passage[p][i])))
        
        p += 1
        #print(passage[p])
        tc = 0
        for e in range(len(passage[p])):
            if passage[p][e] == 0:
                tc+= 1
        if tc == len(passage[p]):
            #print(passage[p])
            break

    #print(passage)
    tot = 0
    for p in passage:
        print(p)
        tot += int(p[-1])

    res.append(tot)
    print(tot)

print(sum(res))