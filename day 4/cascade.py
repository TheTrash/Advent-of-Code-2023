f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]



#l = [ "Card 177: 24 90 40 47 51 75 63 29 57 10 | 49 68 61 43 30 26 84 59 99 75 44 41 17 24 12 38 90 37 36 35 91  9 89 46  8" ]

power = []
test =  {}
for i in range(1,len(l)+1):
    test[i] = 1
print(test)

for row in l:
    matches = 0
    ticket = row.split(":")[1]
    ids = row.split(":")[0]
    my = [ t for t in ticket.split("|")[0].split(" ") if t != '']
    win = [ t for t in ticket.split("|")[1].split(" ") if t != '']
    for curr in my:
        #print(curr, win, curr in win)
        if curr in win:
            matches += 1

    if matches != 0:
        index = int(ids.replace("Card ",""))
        print("card ", index, "wins", matches)
        for i in range(index+1,index+matches+1):
            print(i)
            test[i] += ( 1 * test[index])
            print(test)
        
            
            





print(test)
s = 0
for e in test:
    s+= test[e]
print(s)