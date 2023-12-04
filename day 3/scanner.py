f = open("input", "r")
l = [ n.replace("\n","") for n in f.readlines() ]

symbols = ['%', '/', '-', '*', '$', '&', '+', '#', '=', '@']

matr = []
for row in l:
    tmp = []
    for e in row:
        tmp.append(e)
    matr.append(tmp)

coords = []

for i in range(len(matr)):
    for j in range(len(matr[0])):
        if matr[i][j] in symbols:
            coords.append((i,j))

#print(coords)

tmp_list = []

for curr_pos in coords:
    i_c = curr_pos[0]
    j_c = curr_pos[1]

    queue = []
    for i in range(i_c-1,i_c+2):
        #print("-")
        for j in range(j_c-1,j_c+2):
            #print(matr[i][j])
            if matr[i][j] != "." and matr[i][j] not in symbols:
                queue.append((i,j))
            
    #print(queue)

    appended = True

    while(appended):
        #print("test")
        appended = False       
        for e in queue:
            ## destra
            if ( e[1] < len(matr)  and matr[e[0]][e[1]+1] != "." and matr[e[0]][e[1]+1] not in symbols and (e[0],e[1]+1) not in queue):
                queue.append((e[0],e[1]+1))
                #print(e[0],e[1]+1)
                appended = True
            ## sinistra
            if ( e[1] > 0 and matr[e[0]][e[1]-1] != "." and matr[e[0]][e[1]-1] not in symbols and (e[0],e[1]-1) not in queue):
                queue.append((e[0],e[1]-1))
                #print(e[0],e[1]-1)
                appended = True


    queue.sort()
    ##print(queue)
    st = ""
    


    
    prev = queue[0]
    cut = []
    for i in range(1,len(queue)-1):
        curr = queue[i]
        
        if abs(curr[0] - prev[0]) + abs(curr[1] - prev[1]) > 1:
            cut.append(i)
        prev = curr
    
    cut.append(len(queue)+1)
    #print(cut)
    
    start = 0
    st = ""
    for e in cut:
        for t in queue[start:e]:
            st +=matr[t[0]][t[1]]
        tmp_list.append(int(st))
        st = ""
        start = e

    #print(tmp_list)
print(sum(tmp_list))