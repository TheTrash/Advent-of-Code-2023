import re
f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]


time = [ int(i) for i in l[0].split(":")[1].split(" ") if i != ""]
distance =[ int(i) for i in l[1].split(":")[1].split(" ") if i != ""]
print(time)
print(distance)
tmp = 1
for d , t in zip(distance,time):
    print(d,t)
    c = 0
    for button in range(0,t+1):
        
        dist = button * (t-button)
        if(dist > d):
            print(button, "millisecond", "->", dist)
            c+=1
    tmp *= c
print(tmp)