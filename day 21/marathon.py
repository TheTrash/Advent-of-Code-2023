# Python3 program for the above approach
from collections import deque as queue
import sys

def create_matrix(rows):
    mapp = []
    start = ""
    for i , row in enumerate(rows):
        tmp = []
        for j, e in enumerate(row):
            if e == "S":
                start = (i,j,0)
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
search = 64


# Function to check if a cell
# is be visited or not
def isValid(vis, cell,steps):
	row = cell[0]
	col = cell[1]

	# If cell lies out of bounds
	#if (row < 0  or col < 0  or row > max_i or col > max_j ):
	distanza_x = abs(row - 	search )
	distanza_y = abs(col - 	search )
    # Verifica se le coordinate sono all'interno del rombo

	if not(row in range(max_i) and col in range(max_j)):
		return False


	if manhattan(cell,(start[0],start[1])) > search:
		return False

	# If cell is already visited has to be != from maxint
	if(vis[row][col]) != sys.maxsize or vis[row][col] < search:
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
	vis[start[0]][start[1]] = 0

	# Iterate while the queue
	# is not empty
	steps = 0
	while (len(q) > 0):
		cell = q.popleft()
		x = cell[0]
		y = cell[1]
		steps = cell[2]

		#q.pop()
		steps = steps + 1
		# Go to the adjacent cells
		for i in range(4):
			adjx = x + dRow[i]
			adjy = y + dCol[i]
			if (isValid(vis, (adjx,adjy), steps)):
				#print("char", grid[adjx][adjy], end = " ")
				q.append((adjx, adjy, steps))
				vis[adjx][adjy] = steps



# Driver Code
if __name__ == '__main__':
	###
	###	state is  ( i , j , steps )
	### 

	f = open("input", "r")
	l = [  n.replace("\n","" ) for n in f.readlines()  ]
	# Given input matrix
	grid, start = create_matrix(l)
	max_i , max_j = (len(grid[0])-1,len(grid)-1)
	print(max_i,max_j)

	print(grid, "astart", start)
	# Declare the visited array
	vis = [[ sys.maxsize for i in range(len(grid[0]))] for j in range(len(grid))]
	# vis, False, sizeof vis)

	BFS(grid, vis, start)


	with open('output.txt', 'w+') as f:
		tot = 0
		ma = []
		for row in vis:
			r = ""
			for e in row:
				if e == sys.maxsize:
					r+=" # "
				else:
					if e <= search and e % 2 == 0:
						tot+= 1
					if e < 10:
						r += " "+ str(e) + " "
					else:
						r += str(e)+ " "
			ma.append(r)
			f.write(r+"\n")

	print("part 1" , tot)