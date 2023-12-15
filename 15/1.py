import time
start_time = time.time()

f = open("sample.txt","r").read().split(",")

values = []
for s in f:
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    values.append(v)


print(sum(values))

print("-------  %s seconds -------" % (time.time() - start_time))