import os
from copy import deepcopy
def beauty_print(matr, debug = False):
    if(debug):
        print("\n")
    for i in range(len(matr)):
        row = ""
        for j in range(len(matr[0])):
            row += str(matr[i][j])
        if debug:
            print(row, i)
        else:
            print(row)

def get_neigh(path, cost):
    neigh = []
    point = path[-1]
    old_p = path[-3] if len(path) > 2 else path[-1]
    for di in directions:
        tmp = tuple( t + d for t,d in zip(point, di))
        if 0 <= tmp[0] < len(grid) and 0 <= tmp[1] < len(grid[0]):
            if abs(tmp[0] - old_p[0]) != 3 and abs(tmp[1] - old_p[1]) != 3:
                new_cost = cost + grid[tmp[0]][tmp[1]]
                if tmp in node_dict :
                    if node_dict[tmp] > new_cost :
                        node_dict[tmp] = new_cost
                        neigh.append([ tmp , new_cost])
                else:
                    node_dict[tmp] = new_cost
                    neigh.append([ tmp , new_cost])

    return neigh


def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(int(e))
        mapp.append(tmp)

    return mapp



f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

node_dict = {}

grid = create_matrix(l)
grid2 = create_matrix(l)

su =  ( -1, 0)
giu = (  1, 0)
dx =  (  0, 1)
sx =  (  0,-1)
directions = [su, dx , giu , sx]

#beauty_print(grid)
start = (0,0)
goal = (len(grid)-1,len(grid)-1)

p = start
# inizializzo la fringe solo con la path iniziale
cost = int(grid[p[0]][p[1]])
fringe = [[p, cost, 25 ]]
max_dist = abs(p[0] - goal[0]) + abs(p[1] - goal[1])

sol = []
while(True):
    # estraggo la path che costa meno
    f = min(fringe, key = lambda x : x[1] )
    #print(f)
    fringe.remove(f)
    # p è la path attuale
    p = f[0]
    # cost è il costo della path attuale
    cost = f[1]
    #print(dist)
    sol.append(p)

    if sol[-1] == goal:
        sol.append(f[0])
        break

    # creo le nuove path con le biforcazioni
    ne = get_neigh(sol, cost)
    for n in ne:
        if not(n in fringe):
            fringe.append(n)

    print("fringe", fringe)

for p in sol:
    grid2[p[0]][p[1]] = "X"

print(node_dict)
