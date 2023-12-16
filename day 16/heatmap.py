import os

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


def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return mapp



f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]



# RULES :
# empty space (.), it continues in the same direction
# If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees depending on the angle of the mirror.
# If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space.
# If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing.
def visit(new_path_start):
    total_path = []
    grid = create_matrix(l)
    grid2 = create_matrix(l)
    i= 0
    for path in new_path_start:
        p = path["start"]
        direction = path["direction"]
        direction_char = path["char"]
        
        i+= 1
        while(True):
            #os.system("cls")
            #print("iteration number " , i)
            #grid2[p[0]][p[1]] = direction_char
            grid2[p[0]][p[1]] = "#"

            total_path.append((p, direction))

            if(grid[p[0]][p[1]] == "."):
                pass 
            if(grid[p[0]][p[1]] == "/"):
                if direction == (0,1): # il raggion viene da sx 
                    direction = (-1,0)
                    direction_char = "^"
                elif direction == (0,-1): # il raggion viene da dx
                    direction = (1,0)
                    direction_char = "v"
                elif direction == (1,0) : # il raggio viene da sopra
                    direction = (0,-1)
                    direction_char = "<"
                elif direction == (-1,0): # il raggio viene da sotto
                    direction = (0,1)
                    direction_char = ">"

            if(grid[p[0]][p[1]] == "\\"):
                if direction == (0,1): # il raggion viene da sx
                    direction = (1,0)
                    direction_char = "v"
                elif direction == (0,-1): # il raggion viene da dx
                    direction = (-1,0)
                    direction_char = "^"

                elif direction == (1,0) : # il raggio viene da sopra
                    direction = (0,1)
                    direction_char = ">"
                elif direction == (-1,0): # il raggio viene da sotto
                    direction = (0,-1)
                    direction_char = "<"


            if(grid[p[0]][p[1]] == "|"):
                if direction in [ (1,0), (-1,0) ]: # il raggion viene da sopra o sotto 
                    pass # same direction i dont exist!
                if direction in [ (0,1), (0,-1)]: # il raggion viene da sx o dx
                    # split in due, una viene messa in attesa e l'altra viene proseguita!
                    direction = (-1,0)    # sopra
                    direction_char = "^"
                    t = {"start": p , "direction":(1,0), "char": "v"}
                    if not(t in new_path_start):
                        new_path_start.append({"start": p , "direction":(1,0), "char": "v"}) # il sotto lo appendo e lo proseguo dopo
            if(grid[p[0]][p[1]] == "-"):
                if direction in [ (0,1), (0,-1) ]: # il raggion viene da sopra o sotto 
                    pass # same direction i dont exist!
                if direction in [ (1,0), (-1,0) ]: # il raggion viene da sx o dx
                    # split in due, una viene messa in attesa e l'altra viene proseguita!
                    direction = (0,1)    # destra
                    direction_char = ">"
                    t = {"start": p , "direction":(0,-1), "char": "<"}
                    if not(t in new_path_start):
                        new_path_start.append({"start": p , "direction":(0,-1), "char": "<"}) # sinistra lo appendo e lo proseguo dopo

            #beauty_print(grid2)
            #print(p, direction, len(total_path))

            # check if we are at borders!
            p = tuple( t + d for t,d in zip(p, direction) )
            if not(0 <= p[0] < len(grid) and 0 <= p[1] < len(grid[0])):
                break  # Le coordinate sono fuori dai bordi

            
            if  (p, direction) in total_path:
                break

    tot = 0
    for row in grid2:
        tot+= row.count("#")
    return tot

tmp = create_matrix(l)
su = (-1,0)
giu = (1,0)
dx = ( 0,1)
sx = (0,-1)
directions = [su,giu,dx,sx]
sopra = ( range(len(tmp)), 0)
sotto = ( range(len(tmp)), len(tmp)-1)
sinistra = (0, range(len(tmp)) )
destra = (len(tmp)-1,range(len(tmp)))

sopra_sotto = [sopra, sotto]
sinistra_destra = [sinistra, destra]

res = []
for start in sopra_sotto:
    for i in start[0]:
        for d in directions:
            exp = [{"start": (i,start[1]), "direction": d , "char" : "X" }]
            print(exp)
            t = visit(exp)
            res.append(t)

for start, d in zip(sinistra_destra,(dx,sx)):
    for i in start[1]:
        for d in directions:
            exp = [{"start": (start[0],i), "direction": d , "char" : "X" }]
            print(exp)
            t = visit(exp)
            res.append(t)

print(max(res))

