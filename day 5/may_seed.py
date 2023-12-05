import functools

f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]

almanac = {}

categories = ["seed-to-soil map:" ,"soil-to-fertilizer map:", "fertilizer-to-water map:" , "water-to-light map:","light-to-temperature map:" ,"temperature-to-humidity map:", "humidity-to-location map:" ]
seeds = [ int(n) for n in l[0].replace("seeds: ", "").split(" ")]

many_seeds = [ (seeds[i],seeds[i]+seeds[i+1]-1) for i in range(0,len(seeds),2)]
print("seed calculated!")
#print(many_seeds)

curr_cat = ""
for row in l[2:]:
    if row != "":
        if row in categories:
            curr_cat = row.replace(" map:","")
            almanac[curr_cat] = []
        else:
            almanac[curr_cat].append([ int(n) for n in row.split(" ")])

categories = almanac.keys()

@functools.lru_cache(maxsize=None)
def mapper(item):
    for maps in almanac:
        item = hasher(item,almanac[maps])
    return item

def hasher(item,maps):
    for f in maps:
        if item in range(f[1],f[1]+f[2]):
            i = range(f[1],f[1]+f[2]).index(item)
            return(range(f[0],f[0]+f[2])[i])
    return item

location = []
# prendo inizio, meta e fine di ogni 
# ottengo inizio-mappato, meta-mappato, fine-mappato
# se meta-mappato - inizio mappato == meta - inizio 
# tutto l'array è consecutivo
# il minimo sarebbe inizio




def pivoter(start, end):
    
    p_s = mapper(start)
    p_e = mapper(end)
    #print(start, end, "__" ,p_s, p_e, )
    #print(p_e - p_s == end - start)
    return (p_e - p_s == end - start)



def function(tp):
    global sol
    
    i, m_i, m_f, f = ( tp[0], (tp[0]+tp[1])//2 , (tp[0]+tp[1])//2+1, tp[1] )
    #print(tp)

    if(pivoter(i,m_i)):
        #print("test", i,m_i)
        sol.append((i,m_i))
    else:
        function((i,m_i))

    if(pivoter(m_f,f)) :
        #print("test" , m_f,f)
        sol.append((m_f,f))
    else:
        function((m_f,f))

    return



sol_tot = []

for seed in many_seeds:
    sol = []
    print(seed)
    #print([i for i in range(seed[0],seed[1]+1)])
    #print([mapper(i) for i in range(seed[0],seed[1]+1)])
    function(seed)
    tmp_list = []
    for t in sol:
        if(t[0]==t[1]):
            tmp_list.append(mapper(t[0]))
        else:
            tmp_list.append(mapper(t[0]))
            tmp_list.append(mapper(t[1]))
    sol_tot.append(min(tmp_list))

print(min(sol_tot))