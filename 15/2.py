import time,re
start_time = time.time()

f = open("input.txt","r").read().split(",")

def Hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

boxes = [{} for _ in range(256)]
for s in f:
    ss = re.findall('[a-zA-z]+|\-|\=|\d',s)
    k = ss[0]
    hash = Hash(k)
    match ss[1]:
        case '=':boxes[hash][k]=ss[2]
        case '-':boxes[hash].pop(k,None)

boxValues = [(i+1) * (j+1) * int(b[k]) for i,b in enumerate(boxes) for j,k in enumerate(b)]

print(sum(boxValues))

print("-------  %s seconds -------" % (time.time() - start_time))