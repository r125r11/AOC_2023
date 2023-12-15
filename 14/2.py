import time
start_time = time.time()

f = open("sample.txt","r").read().split("\n")

def rotate_90_degree_anticlckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0]), 0, -1):
        new_matrix.append(list(map(lambda x: x[i-1], matrix)))

    return new_matrix


def rotate_90_degree_clckwise(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(li)

    return new_matrix

f = rotate_90_degree_anticlckwise(f)
rt = 1000000000
rt *= 4
# sequence starting index
ssi = 0
t = 0
uniqueBoards = []
while t < rt:
    for i,l in enumerate(f):
        rpl = {-1:0}
        base = -1
        rc = 0
        for j,c in enumerate(l):
            match c:
                case "O":
                    rpl[base] += 1
                case "#":
                    base = j
                    rpl[base] = 0
                    rc = 0
        keys = list(rpl.keys())
        nl = ''
        for n,k in enumerate(keys):
            if k > -1:
                nl += '#'
            ur = keys[n+1]-1 if n + 1 < len(rpl) else len(l)-1
            empty = ''.join(['.' for _ in range(ur-k-rpl[k])])
            rocks = ''.join(['O' for _ in range(rpl[k])])
            nl+=rocks
            nl+=empty
        f = [*f[:i],nl,*f[i+1:]]

    #found sequence
    if f in uniqueBoards:
        ssi = uniqueBoards.index(f)
        break
    uniqueBoards.append(f)
    f = rotate_90_degree_clckwise(f)
    t += 1

# for i,b in enumerate(uniqueBoards):
#     print('\nboard',i+1,'\n')
#     for l in b: print(l)

# print(ssi, len(uniqueBoards))
sequenceIndex = ssi+(rt-ssi)%(len(uniqueBoards)-ssi)+1
print(sequenceIndex)
f = uniqueBoards[sequenceIndex]
# f = rotate_90_degree_clckwise(f)
# f = rotate_90_degree_clckwise(f)

for l in f:
    print(''.join(l))

sum = 0
for i,l in enumerate(f):
    base = len(l)
    for j,c in enumerate(l):
        match c:
            case "O":
                sum += base
                base -= 1
            case "#":
                base = len(l)-j-1

print(sum)

print("-------  %s seconds -------" % (time.time() - start_time))