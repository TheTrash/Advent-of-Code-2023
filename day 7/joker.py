import functools

f = open("input", "r")
l = [ n.replace("\n", "").split(" ") for n in f.readlines()]

orders = [ "A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J" ]

keys = [ 'high', 'one','two', 'three' ,  'full', 'four', 'five' ]

bucket = {"five" : [], "four": [], "full": [], "three": [], "two": [], "one": [], "high": []}

def count(e, arr):
    return sum([True for i in arr if i == e])

def strength(occ):
    c = max(occ)
    match c:
        case 5:
            return 7
        case 4:
            return 6
        case 3:
            if 2 in occ:
                return 5
            else:
                return 4
        case 2:
            if count(2,occ) == 2:
                return 3
            else:
                return 2
        case 1:
            return 1

def expand(hand):
    from itertools import product
    pos = [i for i,c in enumerate(hand) if hand[i]== "J"]

    from itertools import combinations, permutations, combinations_with_replacement

    # Genera e stampa tutte le combinazioni possibili
    for lunghezza in range(0, len(pos) + 1):
        combinazioni = list(combinations_with_replacement(orders[:-1], lunghezza))
    print(combinazioni)
    li = []
    tmp = list(hand)
    for c in combinazioni:
        for char, i in zip(c,pos):
            tmp[i] = char
        li.append("".join(tmp))
    
    return li

def bucketer_class(occ):
    c = max(occ)
    match c:
        case 5:
            return "five"
        case 4:
            return "four"
        case 3:
            if 2 in occ:
                return "full"
            else:
                return "three"
        case 2:
            if count(2,occ) == 2:
                return "two"
            else:
                return "one"
        case 1:
            return "high"

def bucketer(occ, hand):
    c = max(occ)
    match c:
        case 5:
            bucket["five"].append(hand)
        case 4:
            bucket["four"].append(hand)
        case 3:
            if 2 in occ:
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
    #print("compare" , str1,str2)
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




    # Five of a kind, where all five cards have the same label: AAAAA
    # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    # High card, where all cards' labels are distinct: 23456

def calculate_max_expand(li):
    occur = len(orders) * [0]
    max_strenght = 0
    max_hand = []
    for hand in li:
        for c in hand:
            occur[orders.index(c)] += 1
        
        max_hand.append((hand,strength(occur)))
        occur = len(orders) * [0]
    max_hand = sorted(max_hand,key=lambda x : x[1])
    print(max_hand[-1][1])
    max_hand = [ i for i in max_hand if i[1] == max_hand[-1][1] ]
    print(max_hand)
    return max(max_hand, key=functools.cmp_to_key(compare))

def calculate_occurr(hand):
    occur = len(orders) * [0]
    for c in hand:
        occur[orders.index(c)] += 1
    return occur

for hand in l:
    if 'J' in hand[0]:
        li = expand(hand[0])
        res = calculate_max_expand(li)
        occur = calculate_occurr(res[0])
        print(hand, occur)
        cls = bucketer_class( occur )
        bucket[cls].append(hand)
    else:
        occur = calculate_occurr(hand[0])
        bucketer(occur,hand)
        occur = len(orders) * [0]



rank = 1
tot = 0
#print(bucket)
for b in keys:
    print(bucket[b])
    tmp = sorted(bucket[b],key=functools.cmp_to_key(compare), reverse=True)
#     #print(tmp)
    for i in range(len(bucket[b])-1,-1,-1):
        #print(tmp[i][0] ,tmp[i][1])
        tot += int(tmp[i][1]) * rank
        rank += 1

print(tot)