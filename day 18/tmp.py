string ="(#111620)"

ciph = {0 : "R", 1 : "D", 2 : "L",  3 : "U"}
print(string[-2])
print()
di = ciph[int(string[-2])]
num = int(string[2:-3],16)

print(di, " ", num)