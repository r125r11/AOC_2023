import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

cs = {}
for i,l in enumerate(f):
    cs[i] = 1
for i,l in enumerate(f):
    s=1
    c = l.split(": ")
    c = c[1].split(" | ")
    wn = [int(d) for d in [*c[0].split(" ")] if d != '']
    n = [int(d) for d in [*c[1].split(" ")] if d != '']
    p = [d for d in n if d in wn]
    for y in range(cs[i]):
        if len(p) > 0:
            x = i + 1
            for d in p:
                cs[x] += 1
                x += 1
            # print (s)

print(cs)

s=0
for k in cs:
    s+= cs[k]

print(s)
print("-------  %s seconds -------" % (time.time() - start_time))