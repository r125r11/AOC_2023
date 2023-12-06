import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

t = [int(d) for d in f[0].split(":")[1].split()]
d = [int(n) for n in f[1].split(":")[1].split()]

v = []
for i in range(len(t)):
    r = 0
    for x in range(t[i]):
        if (t[i]-x) * x > d[i]:r +=1
    v.append(r)

print(v)
prod = 1
for d in v: prod *= d
print(prod)

print("-------  %s seconds -------" % (time.time() - start_time))