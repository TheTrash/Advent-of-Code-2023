import re
f = open("input", "r")
board = [ n.replace("\n","") for n in f.readlines() ]

symbols = ['%', '/', '-', '*', '$', '&', '+', '#', '=', '@']

def check(chars,string):
    for c in chars:
        if c in string:
            #print(c,string)
            return True
    return False



tmp_list = []
gear_list = {}
for r, row in enumerate(board):
    nearest = False
    for n in re.finditer(r'\d+', row):
        print(r,n)
        i,j = n.span(0)
        border = []
        for s in (r-1, r, r+1):
            print("s ", s)
            if( -1 < s < len(board) ):
                for t in range(i-1,j+1):
                    if(-1 < t < len(board)):
                        border.append((s,t))
                print(border)

        for bor in border:
            if board[bor[0]][bor[1]] == "*":
                print(board[bor[0]][bor[1]])
                if(bor in gear_list):
                    gear_list[bor].append(int(board[r][i:j]))
                else:
                    gear_list[bor] = [int(board[r][i:j])]

tmp_list = []
print(gear_list)
for e in gear_list:
    if len(gear_list[e]) == 2:
        print(gear_list[e])
        tmp = gear_list[e][0] * gear_list[e][1]
        tmp_list.append(tmp)

print(sum(tmp_list))
        
