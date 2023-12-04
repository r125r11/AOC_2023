import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

g = []
for l in f:
    c = l.split(": ")
    c = c[1].split(" | ")
    wn = [int(d) for d in [*c[0].split(" ")] if d != '']
    n = [int(d) for d in [*c[1].split(" ")] if d != '']
    p = [d for d in n if d in wn]
    if len(p) > 0:
        s = 0.5
        for d in p:
            s *= 2
        print (s)
        g.append(s)

s=0
for d in g:
    s += d

print (s)
print("-------  %s seconds -------" % (time.time() - start_time))