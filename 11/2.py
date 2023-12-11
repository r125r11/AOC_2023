import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

ys = range(len(f))
xs = range(len(f[0]))

coords = []
for y,l in enumerate(f):
    for x,s in enumerate(l):
        if s != ".":
            coords.append([x,y,s])
            ys = [n for n in ys if n != y]
            xs = [n for n in xs if n != x]

offset = 1000000
sum = 0
for i,s in enumerate(coords):
    tcs = coords[i+1:]
    for e in (tcs):
        px = sorted([s[0],e[0]])
        py = sorted([s[1],e[1]])
        diff = px[1]-px[0] + py[1]-py[0]
        for x in xs:
            if px[1] > x and px[0] < x:
                diff += offset-1
        for y in ys:
            if py[1] > y and py[0] < y:
                diff += offset-1
        sum += diff

print(sum)

print("-------  %s seconds -------" % (time.time() - start_time))

# shorter but 2x slower
start_time = time.time()

ys = range(len(f))
xs = range(len(f[0]))

coords = []
for y,l in enumerate(f):
    for x,g in enumerate(l):
        if g != ".":
            coords.append((x,y))
            ys = [n for n in ys if n != y]
            xs = [n for n in xs if n != x]

offset = 1000000
sum = 0
for i,(r,c) in enumerate(coords):
    tcs = coords[i+1:]
    for r2,c2 in (tcs):
        diff = abs(r2-r)+abs(c2-c)
        for x in xs:
            if min(r,r2)<=x<=max(r,r2):
                diff += offset-1
        for y in ys:
            if min(c,c2)<=y<=max(c,c2):
                diff += offset-1
        sum += diff

print(sum)

print("-------  %s seconds -------" % (time.time() - start_time))