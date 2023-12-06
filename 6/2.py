import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

t = [(d) for d in f[0].split(":")[1].split()]
d = [(n) for n in f[1].split(":")[1].split()]

n = ''
for x in t:n +=x
m = ''
for x in d:m +=x

t = int(n)
d = int(m)

v = []
r = 0
for i in range(t):
    if (t-i) * i > d:
        r +=1

print(r)

print("-------  %s seconds -------" % (time.time() - start_time))