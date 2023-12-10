f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]

path = l[0]

starts = []

maze = dict()
tmp = [ i.replace(" = "," ").replace("(","").replace(")","").replace(",","").split(" ")  for i in l[2:]  ]
for t in tmp:
    maze[t[0]] = [ t[1], t[2]]
    if t[0][-1] == "A":
        starts.append(t[0])

rooms = []
print("start", starts)
for start in starts:
    rooms.append(maze[start])

print(rooms)


restart = 1
curr_path = 0



# se finisce 
# ricomincia da capo al RL successivo 

dest = [ 0 for _ in starts ]

mcd_n = []
for start in starts:
    room = start
    node = maze[start]
    steps = 0
    while(room[-1] != "Z"):
        di = path[curr_path]
        #print(di)

        
        # MOVEMENT CODE 
        if(di== "L"): # 1
            room = node[0]
            node = maze[node[0]]
            #print(room,node)
        else:
            room = node[1]
            node = maze[node[1]]

        
        curr_path += 1
        ## check if path is terminated
        if(curr_path == len(path)):
            curr_path = 0
            restart +=1
        steps += 1

    print(room)
    print(steps)

    mcd_n.append(steps)


import math

lcm_result = math.lcm(*mcd_n)
print(lcm_result)