import sys

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



x = { "min" : 4000, "max": 1 , "path": []}
m = { "min" : 4000, "max": 1 }
a = { "min" : 4000, "max": 1 }
s = { "min" : 4000, "max": 1 }

tree = {"A":[],"R":[]}



a_path_rule = []
start = "in"
tree[start] = []
child = [start]


while(child):
    dest = child.pop()
    tree[dest] = []
    for r in rules[dest].replace("{","").replace("}","").split(","):
        rule = r.split(":")
        #print(rule)
        try:
            assert len(rule) == 2, "Last param!"
            tree[dest].append([rule[0],rule[1]])
            if not(rule[1] in  ["A", "R"]):
                child.append(rule[1])
        except AssertionError as msg: 
            tree[dest].append([rule[0]])
            if not(rule[0] in  ["A", "R"]):
                child.append(rule[0])
            
#print(tree)


start = {"x":4000, "m":4000, "a":4000, "s":4000 }

pos = {"x":0, "m":1, "a": 2, "s":3 }



layer = "in"
evaluate = [((1,4000),(1,4000),(1,4000),(1,4000)),layer]

split = tree[layer]
path = [evaluate]
allow = []
while(path):
    evaluate, layer = path.pop()
    split = tree[layer]
    for i in range(len(split)):
        if len(split[i]) > 1:
            rule, dest = split[i]
            tmp = evaluate
            if "x" in rule:
                cut = int(rule[2:])
                if ">" in rule:
                    test = ([((cut+1,tmp[0][1]),tmp[1],tmp[2],tmp[3]),dest]) # true
                    evaluate = ((tmp[0][0],cut),tmp[1],tmp[2],tmp[3])  # false
                elif "<" in rule:
                    test = ([((tmp[0][0],cut-1),tmp[1],tmp[2],tmp[3]),dest]) # true
                    evaluate = ((cut,tmp[0][1]),tmp[1],tmp[2],tmp[3]) # falses
            if "m" in rule:
                cut = int(rule[2:])
                if ">" in rule: 
                    test = ([(tmp[0],(cut+1,tmp[1][1]),tmp[2],tmp[3]),dest]) # true
                    evaluate = (tmp[0],(tmp[1][0],cut),tmp[2],tmp[3])  # false
                elif "<" in rule:
                    test = ([(tmp[0],(tmp[1][0],cut-1),tmp[2],tmp[3]),dest]) # true
                    evaluate = (tmp[0],(cut,tmp[1][1]),tmp[2],tmp[3]) # false
            if "a" in rule:
                cut = int(rule[2:])
                if ">" in rule:
                    test = ([(tmp[0],tmp[1],(cut+1,tmp[2][1]),tmp[3]),dest]) # true
                    evaluate = (tmp[0],tmp[1],(tmp[2][0],cut),tmp[3])  # false
                elif "<" in rule:
                    test = ([(tmp[0],tmp[1],(tmp[2][0],cut-1),tmp[3]),dest]) # true
                    evaluate = (tmp[0],tmp[1],(cut,tmp[2][1]),tmp[3]) # false
            if "s" in rule:
                cut = int(rule[2:])
                if ">" in rule:
                    test = ([(tmp[0],tmp[1],tmp[2],(cut+1,tmp[3][1])),dest]) # true
                    evaluate = (tmp[0],tmp[1],tmp[2],(tmp[3][0],cut))  # false
                elif "<" in rule:
                    test = ([(tmp[0],tmp[1],tmp[2],(tmp[3][0],cut-1)),dest]) # true
                    evaluate = (tmp[0],tmp[1],tmp[2],(cut,tmp[3][1])) # false
            
            if test[1] == "A":
                allow.append(test[0])
            else:
                path.append(test)
        else:
            if split[i][0] == "A":
                allow.append(evaluate)
            elif split[i][0] == "R":
                pass
            else:
                path.append([evaluate,split[i][0]])
        print(test)
        #print(path)


print(allow)

tot = 0
import math

for bord in allow:
    tmp = 1
    for lett in bord:
        #if lett != (1,4000):
        tmp *=  ( lett[1]- lett[0]) +1
    tot+=tmp

print("tot", tot)
# for bord in [x,m,a,s]:
#     tot *=  math.factorial(bord["max"]- bord["min"]) / math.factorial((bord["max"]- bord["min"])-1)
