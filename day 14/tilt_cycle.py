import numpy as np
import copy 
import os
import time
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

    #print(tot)
    return tot

def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return np.array(mapp)


def tilt(matr):
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
action = 0


passage = []
cycle = []
start = False
first_of_cycle = ""
lengt_of_cycle = 0
for i in range(1000000000):
    os.system("cls")
    print("cycle ", i)
    # Rotazione di 90 gradi
    for _ in range(4):
        panel = tilt(panel)
        panel = np.rot90(panel, 3)

    if start == True:
        if panel.tolist() in cycle:
            print(len(cycle))
            break
        cycle.append(panel.tolist())

        

    if panel.tolist() in passage and start == False:
        print(passage.index(panel.tolist()))
        first_of_cycle = panel.tolist()
        start = True
        cycle.append(panel.tolist())

    passage.append(panel.tolist())


    #vis = panel
    #beauty_print(vis)
    #print(result(np.array(panel)))
    #i = input()
    #if i == "e":
    #        break

print(len(passage), len(cycle))
index_of = (1000000000 - 1 - len(passage)-len(cycle)) % len(cycle)
print(index_of)
print(result(np.array(cycle[index_of])))