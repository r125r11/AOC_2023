import time
start_time = time.time()

f = open("input.txt","r").read().split("\n\n")

seeds = [int(d) for d in f[0].split(":")[1].split()]

def findValue(index,vs):
    t = []
    s = []
    d = []
    for l in f[index].split("\n"):
        if l.find(":") > 0:
            continue
        ns = [int(d) for d in l.split()]
        t.append(ns[0])
        s.append(ns[1])
        d.append(ns[2])
    
    rvs = []
    for v in vs:
        found = False
        for i in range(len(s)):
            if v >= s[i] and v <= s[i]+d[i]:
                rvs.append(v-s[i]+t[i])
                found = True
        if found == False:
            rvs.append(v)

    return rvs

ss = findValue(1,seeds)
sf = findValue(2,ss)
fw = findValue(3,sf)
wl = findValue(4,fw)
lt = findValue(5,wl)
th = findValue(6,lt)
lo = findValue(7,th)

print(min(lo))

print("-------  %s seconds -------" % (time.time() - start_time))