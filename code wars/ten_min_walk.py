def is_valid_walk(walk):
    cord = [0,0]
    for d in walk:
        if d == "n":
            cord[1] = cord[1] + 1
        elif d == "s":
            cord[1] = cord[1] - 1
        elif d == "e":
            cord[0] = cord[0] + 1
        elif d == "w":
            cord[0] = cord[0] - 1
            
    return True if (len(walk) == 10) and (cord == [0,0]) else False



def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')