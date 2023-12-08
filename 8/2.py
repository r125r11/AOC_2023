import time,re
from functools import reduce
start_time = time.time()

f = open("input.txt","r").read().split("\n\n")

rules = {}
for line in f[1].split("\n"):
    k,l,r = re.split("[^A-Za-z1-9]+", line)[:3]
    rules[k] = [l,r]

steps = []
for c in f[0]:
    if c == "L": steps.append(0)
    if c == "R": steps.append(1)

keys = [k for k in rules if str(k).endswith('A')]
ts = []
for k in keys:
    key = k
    seeking = True
    step = 0
    while(seeking):
        key = rules[key][steps[step%len(steps)]]
        step+=1; 
        if str(key).endswith('Z'): break
    ts.append(step)

def gcd(a,b): 
    while b: a,b = b, a%b
    return a
def lcm(a,b): return a*b // gcd(a,b)
def lcmm(args): return reduce(lcm, args)

print(lcmm(ts))

print("-------  %s seconds -------" % (time.time() - start_time))