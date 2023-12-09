import time
start_time = time.time()

# ---------- Try one ----------
# f = open("sample.txt","r").read().split("\n")

# s = 0

# def getDiff(values):
#     diff = []
#     for i in range(len(values)-1):
#         diff.append(values[i+1]-values[i])
#     return diff

# def getDiffs(values, items):
#     if all(v == 0 for v in values):
#         return [*items, values]
#     return getDiffs(getDiff(values),[*items, values])


# for l in f:
#     diffs = getDiffs([int(d) for d in l.split()], [])[::-1]
#     for i in range(len(diffs)-1):
#         d = diffs[i]
#         nd = diffs[i+1]
#         nd.append(nd[len(nd)-1]+d[len(d)-1])

#     # print([*diffs[::-1]][0])
#     # print([*[*diffs[::-1]][0]][::-1][0])
#     s += [*[*diffs[::-1]][0]][::-1][0]

# print(s)

# ---------- Clean final ----------
f = open("sample.txt","r").read().split("\n")

s = 0

def getDiff(v): return [v[1:][i] - v[:-1][i] for i in range(len(v[1:]))]

def getDiffs(vs, i): return [*i, vs] if all(v == 0 for v in vs) else getDiffs(getDiff(vs),[*i, vs])

for l in f:
    diffs = getDiffs([int(d) for d in l.split()], [])[::-1]
    for i in range(len(diffs)-1):diffs[i+1].append(diffs[i+1][len(diffs[i+1])-1]+diffs[i][len(diffs[i])-1])
    
    s += [*[*diffs[::-1]][0]][-1]

print(s)

print("-------  %s seconds -------" % (time.time() - start_time))