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

panel = create_matrix(l)
beauty_print(panel)

