import time
start_time = time.time()

f = open("input.txt","r").read().split("\n\n")

def transpose(g):
    ng = ['' for _ in range(len(g[0]))]
    for l in g:
        for i,c in enumerate(l):
            ng[i]+=c
    return ng

def findMirror(g,m):
    for i,_ in enumerate(g):
        if i > 0:
            s = 0
            ui,di = [i-1,i]
            while ui >= 0 and di < len(g):
                u = g[ui]
                d = g[di]
                for j,c in enumerate(d):
                    if c != u[j]:s += 1
                    if s > 1: break
                if s > 1: break
                ui -= 1
                di += 1
            if s == 1: return [m * i, True]

            
    return [0, False]

sum = 0
for g in f:
    g = g.split("\n")
    #lines
    value, found = findMirror(g,100)
    print("vl",value)

    if found == False:
        #columns
        g = transpose(g)
        value, found = findMirror(g,1)
        print("vc",value)

    sum += value

print(sum)
print("-------  %s seconds -------" % (time.time() - start_time))