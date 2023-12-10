

row = "L--J.L7...LJS7F-7L7."

pattern = ["FJ", "L7"]


def count_occurrencies(start,i):
    r = ""
    tmp = 0
    for t in range(start,i):
        r += row[t]

    for p in pattern:
        print("pttern ",p," in ", r.replace("-",""),"  repeat ", r.replace("-","").count(p))
        tmp += r.replace("-","").count(p)
    return tmp

rec = 0
new = ""
start = 0
for i, e in enumerate(row):
    if e == ".":
        rec += count_occurrencies(start,i)
        if rec%2 == 1:
            new += "1"
        else:
            new += "0"
        start = i
    else:
        new += e
print(new)