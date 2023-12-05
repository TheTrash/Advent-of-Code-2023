import re
f = open("input", "r")
l = [ n.replace("\n", "") for n in f.readlines()]

almanac = {}

categories = ["seed-to-soil map:" ,"soil-to-fertilizer map:", "fertilizer-to-water map:" , "water-to-light map:","light-to-temperature map:" ,"temperature-to-humidity map:", "humidity-to-location map:" ]
seeds = [ int(n) for n in l[0].replace("seeds: ", "").split(" ")]
#print(seeds)
curr_cat = ""
for row in l[2:]:
    if row != "":
        if row in categories:
            curr_cat = row.replace(" map:","")
            almanac[curr_cat] = []
        else:
            almanac[curr_cat].append([ int(n) for n in row.split(" ")])

categories = almanac.keys()
#print(almanac)
#print(categories)
# seed         soil
# 53   -soil->  55

# destination start length
#      52       50   48
#   
# 52 -> 50  1
# 53 -> 51  2
# 54 -> 52  3
# 55 -> 53  4
# 56 -> 54  5
# 57 -> 55  6

# se seed compreso tra start e start + length
# allora conversione

def mapper(item,maps):
    #print(maps)
    for f in maps:
        if item in range(f[1],f[1]+f[2]):
            i = range(f[1],f[1]+f[2]).index(item)
            return(range(f[0],f[0]+f[2])[i])
    return item


location = []
for item in seeds:
    for maps in almanac:
        #print(item)
        item = mapper(item, almanac[maps])
    location.append(item)

print(location)
print(min(location))


