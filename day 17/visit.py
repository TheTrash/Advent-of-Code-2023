import os
import sys

from copy import deepcopy
def beauty_print(matr, debug = False):
    if(debug):
        print("\n")
    for i in range(len(matr)):
        row = ""
        for j in range(len(matr[0])):
            row += " " + str(matr[i][j])
        if debug:
            print(row, i)
        else:
            print(row)

def get_neigh(point,old_point):
    neighbor = []
    global unvisited_nodes
    for di in directions:
        tmp = tuple( t + d for t,d in zip(point, di))
        if(tmp in unvisited_nodes):
            if 0 <= tmp[0] < len(grid) and 0 <= tmp[1] < len(grid[0]):
                if abs(tmp[0] - old_point[0]) <= 3 and abs(tmp[1] - old_point[1]) <= 3:
                    neighbor.append(tmp)
                else:
                    print(old_point,point,tmp)
                    print(abs(tmp[0] - old_point[0]), abs(tmp[1] - old_point[1]) )

    return neighbor

def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(int(e))
        mapp.append(tmp)

    return mapp

# Calculating Manhattan Distance from Scratch
def manhattan_distance(point1, point2):
    distance = 0
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance

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

unvisited_nodes = [(i,j) for i in range(len(grid)) for j in range(len(grid))]

def dijkstra_algorithm(graph, start_node):

    global unvisited_nodes
 
    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    current_min_node = start
    # The algorithm executes until we visit all nodes

    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
    
        # The code block below finds the node with the lowest score
        print(current_min_node)
        try:
            # The code block below retrieves the current node's neighbors and updates their distances
            prev = current_min_node
            for _ in range(0,3):
                prev = previous_nodes[prev]
            print("distance", manhattan_distance(current_min_node,prev))
            neighbors = get_neigh(current_min_node, prev)
        except KeyError as e: 
            neighbors = get_neigh(current_min_node, (0,0))
            pass

        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph[neighbor[0]][neighbor[1]]
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


previous_nodes, shortest_path = dijkstra_algorithm(grid,(0,0))

#print(previous_nodes)
print(shortest_path)

tmp = [[ 0 ] * len(grid) for j in range(len(grid))]
#beauty_print(tmp)

node = (len(grid)-1,len(grid)-1)
tot = 0
while(True):
    if node == (0,0):
        break
    else:
        if abs(node[0] - previous_nodes[node][0]) == 1:
            tmp[node[0]][node[1]] = "^"
        if abs(node[1] - previous_nodes[node][1]) == 1:
            tmp[node[0]][node[1]] = "<"
        node = previous_nodes[node]
        tot+= grid[node[0]][node[1]]
beauty_print(tmp)
print(tot)


#print(shortest_path)