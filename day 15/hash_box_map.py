f = open("input", "r")
l = [  n.replace("\n","" ) for n in f.readlines()  ]

actions = l[0].split(",")

lenses = [[] for i in range(256)]

def has(action):
    current_value = 0
    for char in action:
        current_value 
        current_value += ord(char)
        current_value *= 17
        current_value = current_value % 256

    return current_value

tot = 0
for string in actions:
    if "=" in string:
        action = string.split("=")
    if "-" in string:
        action = string.split("-")

    print(action)
    
    index = has(action[0])

    if action[1] != "":
        find = False
        for elem in lenses[index]:
            if elem[0] == action[0]:
                i = lenses[index].index(elem)
                print("modify" , lenses[index][i])
                lenses[index][i] = [action[0], action[1]]
                find = True
        if find == False:
            lenses[index].append([action[0], action[1]])
    else:
        for elem in lenses[index]:
            if elem[0] == action[0]:
                i = lenses[index].index(elem)
                print("remove" , lenses[index][i])
                lenses[index].pop(i)

    
    print([e for e in lenses if e != []] )

tot = 0
for box_index , box in enumerate(lenses):
    for i in range(len(box)):
        tot += ((box_index+1)*(i+1)*int(box[i][1]))
        #print(box_index+1,i+1,box[i][1])

print(tot)