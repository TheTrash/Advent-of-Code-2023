import re
f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]


time = [ i for i in l[0].split(":")[1].split(" ") if i != ""]
distance =[ i for i in l[1].split(":")[1].split(" ") if i != ""]
time = int("".join(time))
distance = int("".join(distance))
print("time", time)
print("distance", distance)




first = 0
for i in range(distance//2):
    if((time-i)*i > distance):
        print(i)
        first = i
        break
print("mid",distance//2)
print((time-first)*(first) > distance)

last = 0
for t in range(first,distance,1):
    if not ((time-t)*t > distance):
        print(t)
        last = t
        break

print(last - first)