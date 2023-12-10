import functools

f = open("input", "r")
l = [ n.replace("\n", "").split(" ") for n in f.readlines()]

orders = [ "A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2" ]

keys = [ 'high', 'one','two', 'three' ,  'full', 'four', 'five' ]

bucket = {"five" : [], "four": [], "full": [], "three": [], "two": [], "one": [], "high": []}

def count(e, arr):
    return sum([True for i in arr if i == e])

def bucketer(occ, hand):
    c = max(occ)
    match c:
        case 5:
            bucket["five"].append(hand)
        case 4:
            bucket["four"].append(hand)
        case 3:
            if 2 in occ:
                print(occ,hand[0])
                bucket["full"].append(hand)
            else:
                bucket["three"].append(hand)
        case 2:
            if count(2,occ) == 2:
                bucket["two"].append(hand)
            else:
                bucket["one"].append(hand)
        case 1:
            bucket["high"].append(hand)

def compare(str1,str2):
    '''
        returns a 
        -1 negative number for less-than
        zero for equality
        1 positive number for greater-than
    '''
    #print(str1,str2)
    for s1,s2 in zip(str1[0],str2[0]):
        #print(s1,s2, "cmp ", 12-orders.index(s1) , 12-orders.index(s2), 12-orders.index(s1) >  12-orders.index(s2))
        if 12-orders.index(s1) == 12-orders.index(s2):
            #print("uguali")
            pass
        elif 12-orders.index(s1) > 12-orders.index(s2): 
            #print(s1,s2, "cmp ", 12-orders.index(s1) , 12-orders.index(s2), 12-orders.index(s1) >  12-orders.index(s2))
            return 1
        else:
            #print(s1,s2)
            return -1


print(l)


    # Five of a kind, where all five cards have the same label: AAAAA
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # High card, where all cards' labels are distinct: 23456

print(compare(['2345A', '1'],['2345J', '3']))

occur = len(orders) * [0]
print(occur)
for hand in l:
    for c in hand[0]:
        occur[orders.index(c)] += 1
    bucketer(occur,hand)
    occur = len(orders) * [0]



rank = 1
tot = 0
print(bucket)
for b in keys:
    #print(bucket[b])
    tmp = sorted(bucket[b],key=functools.cmp_to_key(compare), reverse=True)
    #print(tmp)
    for i in range(len(bucket[b])-1,-1,-1):
        #print(tmp[i][1] , rank)
        tot += int(tmp[i][1]) * rank
        rank += 1

print(tot)