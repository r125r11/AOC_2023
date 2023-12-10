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

dirs = range(4)

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

def checkChar(x,y,d):
    match d:
        case 0: return [x, y-1] if f[y-1][x] == "." else ''
        case 1: return [x+1, y] if f[y][x+1] == "." else ''
        case 2: return [x, y+1] if f[y+1][x] == "." else ''
        case 3: return [x-1, y] if f[y][x-1] == "." else ''

def walkLoop(x,y,d,i):
    sx = x
    sy = y
    sd = d
    c = f[y][x]
    path = [[x,y]]
    while c != "S":
        c = f[y][x]
        match(d):
            case 0:
                if c == "7": 
                    x -= 1
                    d = 3
                if c == "|": 
                    y -= 1
                    d = 0
                if c == "F": 
                    x += 1
                    d = 1
            case 1:
                if c == "J": 
                    y -= 1
                    d = 0
                if c == "-": 
                    x += 1
                    d = 1
                if c == "7": 
                    y += 1
                    d = 2
            case 2:
                if c == "L": 
                    x += 1
                    d = 1
                if c == "|": 
                    y += 1
                    d = 2
                if c == "J": 
                    x -= 1
                    d = 3
            case 3:
                if c == "L": 
                    y -= 1
                    d = 0
                if c == "-": 
                    x -= 1
                    d = 3
                if c == "F": 
                    y += 1
                    d = 2
        path.append([x,y])

    for y in range(len(f)):
        for x in range(len(f[0])):
            if [x,y] not in path: f[y] = f[y][:x] + '.' + f[y][x+1:]

    for l in f:
        print(l)
    x = sx
    y = sy
    d = sd
    cs = []
    c = f[y][x]
    while c != "S":
        c = f[y][x]
        if c == ".": 
            print(x,y,d)
            break
        match(d):
            case 0:
                if c == "7": 
                    if i == 1:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    i = dirs[i-1]
                    if i == 0:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    d = 3
                    x -= 1
                if c == "|": 
                    ic = checkChar(x,y,i)
                    if ic != '' and ic not in cs:cs.append(ic)
                    y -= 1
                    d = 0
                if c == "F": 
                    if i == 3:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    i = dirs[(i+1)%4]
                    if i == 0:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    x += 1
                    d = 1
            case 1:
                if c == "J": 
                    if i == 2:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    i = dirs[i-1]
                    if i == 1:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    y -= 1
                    d = 0
                if c == "-": 
                    ic = checkChar(x,y,i)
                    if ic != '' and ic not in cs:cs.append(ic)
                    x += 1
                    d = 1
                if c == "7": 
                    if i == 0:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    i = dirs[(i+1)%4]
                    if i == 1:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    y += 1
                    d = 2
            case 2:
                if c == "L": 
                    if i == 3:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    i = dirs[i-1]
                    if i == 2:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    x += 1
                    d = 1
                if c == "|":
                    ic = checkChar(x,y,i)
                    if ic != '' and ic not in cs:cs.append(ic)
                    y += 1
                    d = 2
                if c == "J":
                    if i == 1:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic) 
                    i = dirs[(i+1)%4]
                    if i == 2:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    x -= 1
                    d = 3
            case 3:
                if c == "L": 
                    if i == 2:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    i = dirs[(i+1)%4]
                    if i == 3:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    y -= 1
                    d = 0
                if c == "-": 
                    ic = checkChar(x,y,i)
                    if ic != '' and ic not in cs:cs.append(ic)
                    x -= 1
                    d = 3
                if c == "F": 
                    if i == 0:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    i = dirs[i-1]
                    if i == 3:
                        ic = checkChar(x,y,i)
                        if ic != '' and ic not in cs:cs.append(ic)
                    y += 1
                    d = 2
    
    ncs = cs
    for d in cs:
        for x in range(len(f[0])-d[0]):
            c = [d[0]+x,d[1]]
            if f[c[1]][c[0]] == '.':
                if c not in ncs:ncs.append(c)
            else: break
    return ncs

pd = possibleDirections(j,i)
print(pd)
s = []
match(pd[0]):
    case 0: s = walkLoop(j,i-1,0,1)
    case 1: s = walkLoop(j+1,i,1,0)
    case 2: s = walkLoop(j,i+1,2,3)
    case 3: s = walkLoop(j-1,i,3,0)
print(s)
print(len(s))

print("-------  %s seconds -------" % (time.time() - start_time))