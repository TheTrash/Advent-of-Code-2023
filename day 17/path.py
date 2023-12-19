import os
from copy import deepcopy
from heapq import heappop, heappush

from functools import lru_cache
#directions = [ ( -1, 0), (  1, 0),(  0, 1), (  0,-1) ]
directions = [ (0, -1),  (0, 1), (-1, 0),  (1, 0) ]

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

@lru_cache
def get_neigh(cost,point, old_pos, steps):
    print(cost,point, old_pos, steps)
    neigh = []

    tmp = tuple( t + d for t, d in zip(point, old_pos))
    #print(tmp)
    if steps < 3-1 and ( tmp[0] in range(len(grid)) and tmp[1] in range(len(grid))):
        new = ( cost + grid[tmp[0]][tmp[1]] , tmp , old_pos, steps+1 )
        if not(new in visited):
            neigh.append(new)

    if 0 <= steps: 
        for di in directions:
            tmp = tuple( t + d for t, d in zip(point, di))
            if tmp[0] in range(len(grid)) and tmp[1] in range(len(grid)):
                new = ( cost + grid[tmp[0]][tmp[1]] , tmp , di, 0 ) 
                if not(new in visited):
                    neigh.append(new)

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

#beauty_print(grid)
start = (0,0)
goal = (len(grid)-1,len(grid)-1)

# inizializzo la fringe solo con la path iniziale


visited = set()

fringe = []
fringe = get_neigh(0,start,(0,1),0)

while(fringe):
    # creo le nuove path con le biforcazioni

    # estraggo la path che costa meno
    cost, p, pos, steps = heappop(fringe)
    if p == goal:
        print(cost)
        break

    if (cost,p,pos,steps) in visited:
        continue


    visited.add((cost,p,pos,steps))

    ne = get_neigh(cost,p,pos,steps)

    for n in ne:
        #print("vicini di ",(cost,p,pos,steps))
        #print("visited ",visited)
        #print(n)
        if not(n in fringe):
            heappush(fringe,n)


