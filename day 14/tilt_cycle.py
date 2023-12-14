import numpy as np
import copy 

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





def tilt(matr, cicle):
    def swap(rock, free, col):
        matr[rock][col] = "."
        matr[free][col] = "O"

    for col in range(len(matr[0])):
        free_pos = 0
        for i in range(len(matr)):
            if matr[i][col] == "#":
                free_pos = i+1
            if matr[i][col] == "O":
                swap(i,free_pos,col)
                free_pos+=1
    return matr

#beauty_print(panel)
f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

panel = create_matrix(l)

beauty_print(panel)
old_panel = panel
direction = 3
for i in range(4):
    T = np.rot90(panel)
    panel = tilt(T,i)
    
    
    print("cicle ", i%3, "direction ", (i%4))
    beauty_print(np.rot90(T,3-i%4), True)
    print(result(np.rot90(T,3-i%4)))
    #if i%4 == 0:
    #    if (old_panel == np.rot90(panel,i%4)).any():
    #        break
    #    else:
    #        old_panel = new_panel




