import numpy as np

def beauty_print(matr, debug = False):
    if(debug):
        print("\n")
    for i in range(len(matr)):
        row = ""
        for j in range(len(matr[0])):
            row += matr[i][j]
        if debug:
            print(row, i)
        else:
            print(row)

def result(panel):
    tot = 0
    for r in range(len(panel)):
        tot += np.count_nonzero(panel[r][:] == "O") * (len(panel) - r)
        #print(panel[r][:].count("O"))

    print(tot)

def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return np.array(mapp)



def swap(rock, free, col):
    panel[rock][col] = "."
    panel[free][col] = "O"

def tilt():
    for col in range(len(panel[0])):
        free_pos = 0
        for i in range(len(panel)):
            if panel[i][col] == "#":
                free_pos = i+1
            if panel[i][col] == "O":
                swap(i,free_pos,col)
                free_pos+=1


#beauty_print(panel)
f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

panel = create_matrix(l)

beauty_print(panel)

#panel = np.rot90(panel)
tilt()

result(panel)

