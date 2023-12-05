import time
start_time = time.time()

f = open("input.txt","r").read().split("\n\n")

input = [int(d) for d in f[0].split(":")[1].split()]
s = []

i = 0
for x in range(int(len(input)/2)):
    s.append([input[i], input[i+1]])
    i += 2

def findValue(index,vs):
    t = []
    s = []
    d = []
    for l in f[index].split("\n"):
        if l.find(":") > 0:continue
        ns = [int(d) for d in l.split()]
        t.append(ns[0])
        s.append(ns[1])
        d.append(ns[2])
    
    rvs = []
    for v in vs:
        seeking = True
        tv = v
        while(seeking):
            found = False
            for i in range(len(s)):
                # print(tv,s[i],d[i])
                # s<v
                if tv[0] >= s[i] and tv[0] < s[i]+d[i]:
                    # vm<sm
                    found = True
                    if tv[0]+tv[1] <= s[i]+d[i]:
                        # add diff to TV
                        rvs.append([tv[0]-s[i]+t[i], tv[1]])
                        seeking = False
                        break
                    # sm<vm
                    rvs.append([tv[0]-s[i]+t[i],s[i]+d[i]-tv[0]])
                    # tv = [sm, vm - sm]
                    tv = [s[i]+d[i],tv[1]-(s[i]+d[i]-tv[0]-1)]
                    break
                # v<s
                if tv[0] < s[i]:
                    # sm<vm
                    if tv[0]+tv[1] >= s[i] and tv[0]+tv[1] < s[i]+d[i]:
                        found = True
                        rvs.append([t[i],tv[0]+tv[1]-s[i]])
                        tv = [tv[0],s[i]-tv[0]-1]
                        break
                    # v<s-sm<vm
                    if tv[0] + tv[1] > s[i] + d[i]:
                        rvs.append([tv[0]-s[i]+t[i],s[i]-tv[0]])
                        rvs.append([t[i],d[i]])
                        tv = [s[i]+d[i],tv[0]+tv[1]-s[i]-d[i]-1]
                        break
            if found == False: rvs.append(tv); seeking=False; break
    return rvs

print("step soil")
ss = findValue(1,s)
print("step fert")
sf = findValue(2,ss)
print("step wat")
fw = findValue(3,sf)
print("step lig")
wl = findValue(4,fw)
print("step tem")
lt = findValue(5,wl)
print("step hum")
th = findValue(6,lt)
print("step loc")
lo = findValue(7,th)

mm = lo[0][0]
for l in lo:
    if l[0] < mm:
        mm = l[0]
print(min(lo))

print("-------  %s seconds -------" % (time.time() - start_time))