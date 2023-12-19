import re

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

f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

terrain = [[ "." for i in range(10)] for j in range(10)]


directions = { "U": ( -1, 0), "D":(  1, 0), "R":(  0, 1), "L":(  0,-1) }


curr = (0,0)
#terrain[curr[0]][curr[1]] = "#"
coords = []
for row in l:
    di , le , color = row.split(" ")
    #print(di , le , color)
    for i in range(int(le)):
        curr = tuple( t + d for t, d in zip(curr, directions[di]))
        #terrain[curr[0]][curr[1]] = "#"
        coords.append(curr)



min_i = min(coords, key= lambda x: x[0])
max_i = max(coords, key= lambda x: x[0])
min_j = min(coords, key= lambda x: x[1])
max_j = max(coords, key= lambda x: x[1])
print("min_i: ",min_i,"max_i: ", max_i,"min_j: ", min_j,"max_j: ",max_j)

print(min(coords))
print(max(coords))
border_min = (max_i[0], min_j[1])
border_max = (min_i[0], max_j[1])
print(border_min)
print(border_max)

last_flag = 0
new_coords = []
for b in coords:
    new_coords.append((b[0]+abs(min_i[0]),b[1]+abs(min_j[1])))

min_i = min(new_coords, key= lambda x: x[0])
max_i = max(new_coords, key= lambda x: x[0])
min_j = min(new_coords, key= lambda x: x[1])
max_j = max(new_coords, key= lambda x: x[1])
print("min_i: ",min_i,"max_i: ", max_i,"min_j: ", min_j,"max_j: ",max_j)

print(min(new_coords))
print(max(new_coords))
border_min = (max_i[0], min_j[1])
border_max = (min_i[0], max_j[1])
print(border_min)
print(border_max)



import numpy as np
import cv2

terrain = [[ 0 for i in range(max_j[1]+1)] for j in range(max_i[0]+1)]

for curr in new_coords:
    terrain[curr[0]][curr[1]] = 255
#beauty_print(terrain)

with open("matrix.txt", "w+") as textFile:
    for row in terrain:
        textFile.write(' '.join([str(a) for a in row]) + '\n')

contours = np.array( new_coords )
tmp = np.array( terrain ) # create a single channel 200x200 pixel black image 

print("points",(max_i[0]+1,max_j[1]+1))
print("shape",tmp.shape)

img = np.zeros( (tmp.shape[1],tmp.shape[0]) ) # create a single channel 200x200 pixel black image 
cv2.fillPoly(img, pts =[ contours ], color=(255,255,255), lineType= cv2.LINE_4 )
cv2.imshow(" ", img)
cv2.waitKey()

with open("matrix_img.txt", "w+") as textFile:
    for row in img:
        textFile.write(' '.join(["#" if a == 255 else "." for a in row]) + '\n')

print(img[0])
tmp = 0
for row in img:
    tmp += np.sum(row==255)
print(tmp)