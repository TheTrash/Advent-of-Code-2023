import re
f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]


time = [ i for i in l[0].split(":")[1].split(" ") if i != ""]
distance =[ i for i in l[1].split(":")[1].split(" ") if i != ""]
time = int("".join(time))
distance = int("".join(distance))
print(time)
print(distance)
