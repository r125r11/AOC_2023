import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

i = 0
j = 0
done = False
for l in f:
    j = 0
    for c in l:
        if c == "S": done = True; break
        j += 1
    if done == True: break
    i += 1

print(i,j)

def possibleDirections(x,y):
    dirs = []
    # up
    if y > 0 and (f[y-1][x] in ["|","7","F"]): dirs.append(0)
    # right
    if x < len([f[0]][0]) and (f[y][x+1] in ["-","7","J"]): dirs.append(1)
    # down
    if y < len(f[0]) and (f[y+1][x] in ["|","J","L"]): dirs.append(2)
    # left
    if x > 0 and (f[y][x-1] in ["-","L","F"]): dirs.append(3)
    return dirs

def walkLoop(x,y,d,s):
    c = f[y][x]
    while c != "S":
        c = f[y][x]
        if c == ".": 
            print(x,y,d)
            break
        match(d):
            case 0:
                if c == "7": 
                    x -= 1
                    d = 3
                    s += 1
                if c == "|": 
                    y -= 1
                    d = 0
                    s += 1
                if c == "F": 
                    x += 1
                    d = 1
                    s += 1
            case 1:
                if c == "J": 
                    y -= 1
                    d = 0
                    s += 1
                if c == "-": 
                    x += 1
                    d = 1
                    s += 1
                if c == "7": 
                    y += 1
                    d = 2
                    s += 1
            case 2:
                if c == "L": 
                    x += 1
                    d = 1
                    s += 1
                if c == "|": 
                    y += 1
                    d = 2
                    s += 1
                if c == "J": 
                    x -= 1
                    d = 3
                    s += 1
            case 3:
                if c == "L": 
                    y -= 1
                    d = 0
                    s += 1
                if c == "-": 
                    x -= 1
                    d = 3
                    s += 1
                if c == "F": 
                    y += 1
                    d = 2
                    s += 1
    return s

pd = possibleDirections(j,i)
print(pd)
s = 0
match(pd[0]):
    case 0: s = walkLoop(j,i-1,0,1)
    case 1: s = walkLoop(j+1,i,1,1)
    case 2: s = walkLoop(j,i+1,2,1)
    case 3: s = walkLoop(j-1,i,3,1)
print(s)

print("-------  %s seconds -------" % (time.time() - start_time))