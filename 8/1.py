import time,re
start_time = time.time()

f = open("input.txt","r").read().split("\n\n")

rules = {}
for line in f[1].split("\n"):
    k,l,r = re.split("[^A-Za-z]+", line)[:3]
    rules[k] = [l,r]

steps = []
for c in f[0]:
    if c == "L": steps.append(0)
    if c == "R": steps.append(1)

seeking = True
step = 0
key = 'AAA'
while(seeking):
    key = rules[key][steps[step%len(steps)]]
    step+=1; 
    if key == 'ZZZ': break

print(step)

print("-------  %s seconds -------" % (time.time() - start_time))