f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]




maze = []



def vicinato(point):
    ''' i vicinati in cui si può effettivamente andare sono:
      per top avremo 7 | F
      per down avremo J | L

      per left L - F
      per rigth J - 7
    '''
    vic = []
    y = point[0]
    x = point[1]
    if maze[y-1][x] in ["7", "|", "F"]:
        vic.append((y-1,x))
    if maze[y+1][x] in ["J", "|" ,"L"]:
        vic.append((y+1,x))

    if maze[y][x-1] in ["L", "-", "F"]:
        vic.append((y,x-1))

    if maze[y][x+1] in ["7", "-", "J"]:
        vic.append((y,x+1))

    return vic


start = (0,0)

for j, row in enumerate(l):
    tmp = []
    for i, e in enumerate(row):
        if e == "S":
            start = (i,j)
        tmp.append(e)
    maze.append(tmp)

for row in maze:
    print(row)

print(start)
print(vicinato(start))

curr = start
path = []
max_dist = 0
max_node = ""

print("vicinato 1,2 ",  vicinato((1,2)))

i = 0
while(i != 2):
    vic = vicinato(curr)
    print(maze[curr[0]][curr[1]])
    print(vic)
    print(curr)


    if len(path) == 0:
        curr = vic[1]
    for vi in vic:
        if vi not in path:
            curr = vi
            break
    path.append(curr)


    if start == curr:
        break
    i+=1