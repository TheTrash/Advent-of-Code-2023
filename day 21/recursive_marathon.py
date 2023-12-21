# Python3 program for the above approach
from collections import deque as queue
from copy import deepcopy
import sys
import numpy as np


def create_matrix(rows):
    mapp = []
    start = ""
    for i , row in enumerate(rows):
        tmp = []
        for j, e in enumerate(row):
            if e == "S":
                start = (i,j)
            tmp.append(e)
        mapp.append(tmp)

    return mapp, start

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

# Direction vectors
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

max_i = 0
max_j = 0
search = 10


# Function to check if a cell
# is be visited or not
def isValid(vis, cell):
	row = cell[0]
	col = cell[1]
	steps = cell[2]
	xn = cell[3]
	yn = cell[4]

	# If cell lies out of bounds
	#if (row < 0  or col < 0  or row > max_i or col > max_j ):
	distanza_x = abs(row - 	search )
	distanza_y = abs(col - 	search )
    # Verifica se le coordinate sono all'interno del rombo

	if steps > search:
		return False

	if not(row in range(max_i) and col in range(max_j)):
		return False


	# if manhattan(cell,(start[0],start[1])) > search:
	# 	return False

	# If cell is already visited has to be != from maxint
	print(vis[xn][yn][row][col])
	if(vis[xn][yn][row][col]) != sys.maxsize or vis[xn][yn][row][col] < search:
		return False


	if (grid[row][col] == "#"):
		return False

	# Otherwise
	return True

# Function to perform the BFS traversal
def BFS(grid, vis, start):

	# Stores indices of the matrix cells
	q = queue()

	# Mark the starting cell as visited
	# and push it into the queue
	q.append(start)

	# Iterate while the queue
	# is not empty
	steps = 0
	while (len(q) > 0):
		cell = q.popleft()
		x = cell[0]
		y = cell[1]
		steps = cell[2]
		xn = cell[3]
		yn = cell[4]


		steps = steps + 1
		# Go to the adjacent cells
		for i in range(4):
			if x + dRow[i] > max_i:
				adjx = (x + dRow[i])%max_i
				xn+=1
			elif x + dRow[i] < 0:
				adjx = (x + dRow[i])%max_i
				xn-=1
			else:
				adjx = x + dRow[i]
			if y + dCol[i] > max_j:
				adjy = (y + dCol[i])%max_j
				yn +=1
			elif y + dCol[i] < 0:
				adjy = (y + dCol[i])%max_j
				yn -=1
			else:
				adjy = y + dCol[i]

			print((adjx,adjy,steps,xn,yn))
			if (isValid(vis, (adjx,adjy,steps,xn,yn))):
				q.append((adjx, adjy, steps,xn,yn))
				vis[xn][yn][adjx][adjy] = steps



# Driver Code
if __name__ == '__main__':
	###
	###	state is  ( i , j , steps )
	### 

	f = open("test", "r")
	global empty_vis 
	l = [  n.replace("\n","" ) for n in f.readlines()  ]
	# Given input matrix
	grid, start = create_matrix(l)
	max_i , max_j = (len(grid[0])-1,len(grid)-1)
	print(max_i,max_j)
	start = (start[0],start[1],0,max_i//2,max_j//2)
	print(grid, "astart", start)
	# Declare the visited array
	vis= [[sys.maxsize for i in range(100)] for j in range(100)]
	for i in range(100):
		for j in range(100):
			vis[i][j] = [[sys.maxsize for i in range(max_i)] for j in range(max_j)]




	# vis, False, sizeof vis)

	BFS(grid, vis, start)


	with open('output.txt', 'w+') as f:
		tot = 0
		parity = 0
		for table in vis:
			for row in table:
				parity = (parity+1)%2
				for i in row:
					r = ""
					for e in i:
						if e == sys.maxsize:
							r+=" # "
						else:
							if e <= search and e % 2 == parity:
								tot+= 1
							if e < search:
								r += " "+ str(e) + " "
							else:
								r += str(e)+ " "

	print("part 1" , tot)