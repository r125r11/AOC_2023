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
    for i,l in enumerate(g):
        if i > 0:
            if l == g[i-1]:
                # edge cases
                if i == 1 or i == len(g)-1:return [m * i, True]

                isMirror = True
                ui,di = [i-2,i+1]
                while ui >= 0 and di < len(g):
                    if g[ui] != g[di]:
                        isMirror = False
                        break
                    ui -= 1
                    di += 1

                if isMirror:
                    return (m * i, True)
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