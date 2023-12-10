f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]

path = l[0]

maze = dict()
tmp = [ i.replace(" = "," ").replace("(","").replace(")","").replace(",","").split(" ")  for i in l[2:]  ]
for t in tmp:
    maze[t[0]] = [ t[1], t[2]]


goal = "ZZZ"
room = "AAA"
node = maze["AAA"]


restart = 1
curr_path = 0



# se finisce 
# ricomincia da capo al RL successivo 
steps = 0

while(room != goal):
    di = path[curr_path]
    print(di)
    #print(room)
    #print(maze[room])

    
    # MOVEMENT CODE 
    if(di== "L"): # 1
        room = node[0]
        node = maze[node[0]]
        print(room,node)
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
