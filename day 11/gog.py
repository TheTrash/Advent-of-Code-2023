f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

galaxy = []


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
    
print(galaxy)

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

beauty_print(galaxy)

print("____________________")
expanded = []
new = ['.' for _ in range(len(galaxy[0]))]
for i in range(len(galaxy)):
    tmp = ""
    expanded.append(galaxy[i])
    if i in expand["row"]:
        expanded.append(new)

beauty_print(expanded)

expanded_T = transpose(expanded)
print("____________________")
expanded_last = []
new = ['.' for _ in range(len(expanded_T[0]))]
for i in range(len(expanded_T)):
    tmp = ""
    expanded_last.append(expanded_T[i])
    if i in expand["col"]:
        expanded_last.append(new)

res = transpose(expanded_last)

beauty_print(res)

galaxys = []

for i in range(len(res)):
    for j in range(len(res[0])):
        if res[i][j] == "#":
            galaxys.append((i,j))


print(manhattan_distance((4,0),(10,9)))

print(galaxys)
s = 0


from itertools import combinations

temp = combinations(galaxys,2)
for i in list(temp):
    s += manhattan_distance(i[0],i[1])

print(s)