f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]


directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

ciph = { 0 : "R", 1 : "D", 2 : "L",  3 : "U"}

coords = []

x = 0
y = 0
perimeter = 0
for row in l:
    _ , _ , color = row.split(" ")

    di = ciph[int(color[-2])]
    le = int(color[2:7],16)


    dx, dy = directions[di]
    x += dx * le
    y += dy * le
    perimeter += le
    coords.append((x, y))


area = 0
ox, oy = coords[0]
for x, y in coords[1:]:
    area += (x * oy - y * ox)
    ox, oy = x, y


area = abs(area // 2) + perimeter // 2 + 1
print("sol:", area)


