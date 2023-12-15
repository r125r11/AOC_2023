import time
start_time = time.time()

f = open("sample.txt","r").read().split(",")
f1 = [*f]

values = []
for s in f:
    v = 0
    for c in s: v = ((v + ord(c)) * 17)%256
    values.append(v)

print(sum(values))

print("-------  %s seconds -------" % (time.time() - start_time))