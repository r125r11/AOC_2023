import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")
values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]

hands = {
    1:[],
    2:[],
    22:[],
    3:[],
    32:[],
    4:[],
    5:[],
}

def insertInHands(hand, key, value, og):
    hs = hands[key]
    hs.append([hand, value, og])
    hands[key] = sorted(hs)

def determineValue(hand):
    h = {}
    for c in hand: h[c] = h[c] + 1 if c in h else 1
    
    h = dict(sorted(h.items(), key=lambda item: item[1],reverse=True))

    keys = [k for k in h]

    if 0 in h:
        if h[0] == 5 or h[0] == 4: return 5
        if h[0] == 3:
            if h[keys[1]] == 2: return 5
            if h[keys[1]] == 1: return 4
        if h[0] == 2:
            if h[keys[0]] == 3: return 5
            if h[keys[0]] == 2: 
                if h[keys[1]] == 2:return 4
                if h[keys[1]] == 1:return 3
            if h[keys[1]] == 1: return 3
        if h[0] == 1:
            if h[keys[0]] == 4: return 5
            if h[keys[0]] == 3: return 4
            if h[keys[0]] == 2: 
                if h[keys[1]] == 2: return 32
                return 3
            if h[keys[0]] == 1: return 2
            
    else:
        if h[keys[0]] == 1: return 1
        if h[keys[0]] == 2 and h[keys[1]] == 1: return 2
        if h[keys[0]] == 2 and h[keys[1]] == 2: return 22
        if h[keys[0]] == 3 and h[keys[1]] == 1: return 3
        if h[keys[0]] == 3 and h[keys[1]] == 2: return 32
        if h[keys[0]] == 4: return 4
        return 5

def resolveHand(hand, value):
    ih = []
    for c in hand:ih.append(*[i for i,v in enumerate(values) if c == v])
    insertInHands(ih,determineValue(ih), int(value), hand)

[(resolveHand(h,v)) for h,v in [l.split(" ") for l in f]]

sum = 0
i = 1
for p in hands:
    for h in hands[p]:
        sum += h[1]*i
        i += 1

print(sum)

print("-------  %s seconds -------" % (time.time() - start_time))