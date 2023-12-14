first = ["..#..#..##..#..#.",".######.#.....##."]
second = ["#.#..#..##..#..#.",".######.#.....##."]
first = [e for e in first]
second = [e for e in second]

def find_smudge(window_1,window_2):
    smudge = 0
    for r1, r2 in zip(window_1,window_2):
        for e1, e2 in zip(r1,r2):
            print(e1,e2)
            if e1 != e2:
                smudge += 1 
    print(smudge)
    if smudge in (0,1):
        return True
    else:
        return False
    
find_smudge(first,second)