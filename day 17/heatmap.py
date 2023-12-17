import seaborn as sns
import matplotlib as plt
def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(int(e))
        mapp.append(tmp)

    return mapp



f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

grid = create_matrix(l)
goal = (len(grid)-1,len(grid)-1)

matr_dist = []
for i in range(len(grid)):
    tmp = []
    for j in range(len(grid)):
        tmp.append(len(grid) - (abs(i - goal[0]/2) + abs(j - goal[1]/2)) )
    matr_dist.append(tmp)

sns.heatmap(matr_dist, annot=True)
# giving title to the plot 