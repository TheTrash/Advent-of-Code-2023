f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

galaxy = []
years = 1000000

def manhattan_distance(point1, point2):
    return sum([abs(point1[0] - point2[0]), abs(point1[1]-point2[1])])


def beauty_print(matr):
    for i in range(len(matr)):
        row = ""
        for j in range(len(matr[0])):
            row += matr[i][j]
        print(row)

def  transpose(matr):
    return list(map(list, zip(*matr)))


for i, row in enumerate(l):
    tmp = []
    for j, e in enumerate(row):
        tmp.append(e)
    #print(tmp)
    galaxy.append(tmp)
    
#print(galaxy)

expand = {"col" : [], "row" : []}
for i in range(len(galaxy)):
    row = ""
    col = ""
    for j in range(len(galaxy[0])):
        row += galaxy[i][j]
        col += galaxy[j][i]

    if row.count(".") == len(row):
        #print("row", i)
        expand["row"].append(i)
        pass
    if col.count(".") == len(col):
        #print( i)
        expand["col"].append(i)
        pass


galaxyes = []

for i in range(len(galaxy)):
    for j in range(len(galaxy[0])):
        if galaxy[i][j] == "#":
            galaxyes.append((i,j))



from itertools import combinations

new_coords = []
print(galaxyes)
print(expand)
for galaxy in galaxyes:
    tmp = [galaxy[0], galaxy[1]]
    for ex in expand["row"]:
        if galaxy[0] > ex:
            tmp[0] += years-1

    for ex in expand["col"]:
        if galaxy[1] > ex:
            tmp[1] += years-1

    new_coords.append(tuple(tmp))

print(new_coords)



s = 0
temp = combinations(new_coords,2)
for i in list(temp):
    s += manhattan_distance(i[0],i[1])

print(s)