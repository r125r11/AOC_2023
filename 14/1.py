import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

def transpose(g):
    ng = ['' for _ in range(len(g[0]))]
    for l in g:
        for i,c in enumerate(l):
            ng[i]+=c
    return ng

f = transpose(f)

sum = 0
# rpl = {}
for i,l in enumerate(f):
    # rpl[i] = {}
    base = len(l)
    for j,c in enumerate(l):
        match c:
            case "O":
                sum += base
                base -= 1
            case "#":
                base = len(l)-j-1

print(sum)

print("-------  %s seconds -------" % (time.time() - start_time))