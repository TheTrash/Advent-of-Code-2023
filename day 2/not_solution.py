

def total_box_counter(row):
    box_total = { "red": 0, "green": 0 ,  "blue": 0 }
    for box in boxes:
        res = [i for i in range(len(row)) if row.startswith(box, i)]
        if res != []:
            for e in res:
                i = e
                while( i != 0 and row[i] != ',' and row[i] != ';' ):
                    i -= 1
                i+=1
                tmp = row[i:e].replace(" ","")
                num = int(tmp)
                if box in box_total:
                    box_total[box] += num

    return box_total



f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]

boxes = ["red", "green",  "blue"]
eval_test = { "red": 12, "green": 13 ,  "blue": 14 }



ids = []
for riga in l:
    ids_i = riga.split(":")[0]
    row = riga.split(":")[1]
     
    train = total_box_counter(row)
    
    if train["red"] <= eval_test["red"] and train["green"] <= eval_test["green"] and train["blue"] <= eval_test["blue"]:
        print(train)
        ids.append(int(ids_i.replace("Game","").replace(" ","")))
  
print(ids)
print(sum(ids))