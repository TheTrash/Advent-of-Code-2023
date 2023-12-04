

def box_checker(row):
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
                if eval_test[box] < num:
                    return False
    return True



f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]

boxes = ["red", "green",  "blue"]
eval_test = { "red": 12, "green": 13 ,  "blue": 14 }



ids = []
for riga in l:
    ids_i = riga.split(":")[0]
    row = riga.split(":")[1]
     
    
    
    if box_checker(row):
        ids.append(int(ids_i.replace("Game","").replace(" ","")))
  
print(ids)
print(sum(ids))