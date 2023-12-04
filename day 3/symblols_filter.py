f = open("input", "r")
l = [ n.replace("\n","") for n in f.readlines() ]

numbers = ["1","2","3","4","5","6","7","8","9"]

symbols = []
for e in l:
    for i in e:
        if i not in numbers or i !=".":
            symbols.append(i)

print(list(dict.fromkeys(symbols)))