with open("input") as f:
    puzzle = f.read()

def parse_block(block):
    L = []
    for line in block.splitlines():
        L.append([ c for c in line])
    return L


def parse_data(data):
    return [parse_block(block) for block in data.split("\n\n")]

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

def stampa_prima_meta(matrice,stop):
    matr = []
    righe = len(matrice)

    # Calcola la posizione di mezzo delle righe
    meta_righe = stop

    # Stampa la prima metà orizzontale della matrice
    for i in range(meta_righe+1):
        matr.append(matrice[i])

    return matr

def stampa_seconda_meta(matrice, start):
    matr = []
    # Calcola il numero di righe della matrice
    righe = len(matrice)

    # Calcola la posizione di inizio della seconda metà
    inizio_seconda_meta = start

    # Stampa la seconda metà orizzontale specchiata della matrice
    for i in range(inizio_seconda_meta, righe):
        matr.append(matrice[i])
    
    return matr[::-1]
    #return matr

def find(matr, debug = False):
    f = False
    lez = len(matr)
    for le in range(0,lez):
        first = stampa_prima_meta(matr,le)
        second = stampa_seconda_meta(matr,le+1)

        #beauty_print(first)
        #print("[sep]")
        #beauty_print(second)
        #print("[sep]")
        if len(first) > len(second):
            window_fi = first[len(first)-len(second):]
            window_se = second
        else:
            window_fi = first
            window_se = second [len(second)-len(first):]
        if debug:
            print("      ")
            beauty_print(window_fi)
            print("------------  mirror", le+1)
            beauty_print(window_se[::-1])


        if ( len(window_fi) != 0 and len(window_se) != 0 ) and window_fi == window_se:
            if debug:
                print("      ")
                beauty_print(window_fi)
                print("------------  mirror", le+1)
                beauty_print(window_se[::-1])
                print("equal")
            f = True
            break

    return f, le+1

def create_matrix(rows):
    mapp = []
    for row in rows:
        tmp = []
        for e in row:
            tmp.append(e)
        mapp.append(tmp)

    return mapp

start = 0

tot = 0
for mapp in parse_data(puzzle):
    beauty_print(mapp)
    res = find(mapp, True)
    if res[0] == True:
        #print("orizontal", res)
        tot += res[1] * 100
    else:
        mapp = [[mapp[j][i] for j in range(len(mapp))] for i in range(len(mapp[0]))]
        res = find(mapp, True)
        #print("vertical", res)
        if res[0] == False:
            beauty_print(mapp)
        tot += res[1] 

print(tot)