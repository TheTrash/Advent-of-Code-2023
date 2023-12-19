f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

tmp = 0

rules = {}
pieces = []
for row in l:
    if row == "":
        tmp+=1
        continue
    
    if tmp == 0:
        r = row.replace("}","").split("{")
        print(r)
        rules[r[0]] = r[1:][0]
    else:
        row = row.replace("{","").replace("}","").split(",")
        var = [
            int(row[0].replace("x=","")),
            int(row[1].replace("m=","")),
            int(row[2].replace("a=","")),
            int(row[3].replace("s=",""))
        ]
        pieces.append(var)

print(rules)
print(pieces)


tot = 0
for piece in pieces:
    x,m,a,s = piece
    print(x,m,a,s)

    dest = "in"
    while(True):
        print(dest)
        for r in rules[dest].replace("{","").replace("}","").split(","):
            rule= r.split(":")
            try:
                assert len(rule) == 2, "Last param!"
                if(eval(rule[0])):
                    dest = rule[1]
                    break
            except AssertionError as msg: 
                dest = rule[0]
        if dest == "A":
            print("ACCEPTED")
            tot += sum(piece)
            break
        if dest == "R":
            print("rejected")
            break

print(tot)