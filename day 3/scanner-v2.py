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
            print(bor)
            if board[bor[0]][bor[1]] in symbols:
                print(board[bor[0]][bor[1]])
                nearest = True
       
        
        if nearest:
            tmp_list.append(int(board[r][i:j]))
            nearest = False

print(tmp_list)
print(sum(tmp_list))
        

