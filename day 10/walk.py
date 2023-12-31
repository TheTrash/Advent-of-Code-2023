f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]


d = {"L": [(-1,0), (0,1)] ,"|":[(-1,0),(1,0)],"-": [(0,-1),(0,1)], "F":[(1,0),(0,1)] ,"7":[(1,0),(0,-1)], "J": [(-1,0),(0,-1)],  ".":[]}


maze = []
path = []

def first_vicinate(start):
    vic = []
    y = start[0]
    x = start[1]
    for i in (y-1,y+1):
        if start in vicinato((i,x)):
            vic.append((i,x))
    for j in (x-1,x+1):
        if start in vicinato((y,j)):
            vic.append((y,j)) 
    
    return vic


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
    tile = maze[y][x]
    #print("tile", tile)
    for tmp in d[tile]:
        #print(tmp)
        vic.append(tuple([sum(x) for x in zip(tmp,point)]))

    return vic




## modificare walk in modo che dato un punto restituisca il successivo 
# nel main loop fare walk(left) walk(right) finché left e right non sono uguali
# tac 
def walk(point, path):
    vic = vicinato(point)
    for v in vic:
        if not(v in path):
            #print(v)
            return v
    else:
        return (0,0)



## maze creation
for i, row in enumerate(l):
    tmp = []
    for j, e in enumerate(row):
        if e == "S":
            start = (i,j)
        tmp.append(e)
    maze.append(tmp)

left_path = []
right_path = []

steps = 1
print(start)
left_path.append(start)
right_path.append(start)
starts = first_vicinate(start)

left_path.append(starts[0])
right_path.append(starts[1])

while(True):
    right = right_path[-1]
    left = left_path[-1]
    if(left == right):
        print(steps)
        break

    left_path.append(walk(right,left_path))
    right_path.append(walk(left,right_path))
    steps +=1
    
#print(left_path,right_path)