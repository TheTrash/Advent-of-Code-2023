import os
from copy import deepcopy
from heapq import heappop, heappush

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

def get_neigh(point, cost, old_cout):
    neigh = []
    for di, cout in zip(directions,["A","B","C","D"]):
        tmp = tuple( t + d for t,d in zip(point, di))
        if tmp[0] in range(len(grid)) and tmp[1] in range(len(grid)) and not(tmp in visited):
            if not(old_cout in [ i*3 for i in ["A","B","C","D"]]):
                new_cost = cost + grid[tmp[0]][tmp[1]]
                neigh.append(( tmp , new_cost, old_cout[-2:]+cout ))

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

# inizializzo la fringe solo con la path iniziale
p = start
cost = 0

fringe = [(p, cost ,"")]
visited = []

while(fringe):
    # estraggo la path che costa meno
    p, cost, di = heappop(fringe)

    if p == goal:
        print(cost)
        break

    # creo le nuove path con le biforcazioni
    visited.append(p)
    ne = get_neigh(p,cost,di)
    for n in ne:
        print("vicini di ",p,"\n",n)
        print("visited ",visited)
        if not((n[0]) in visited):
            if len(fringe) > 0:
                if not(n[0] in fringe[:][0]):
                    heappush(fringe,n)
            else:
                heappush(fringe,n)

    print("fringe", fringe)

    inp = input()

