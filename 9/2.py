import time
start_time = time.time()

# ---------- Try one ----------
# f = open("input.txt","r").read().split("\n")

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
#         ld = diffs[i+1][::-1]
#         pld = diffs[i][::-1]
#         ld.append(ld[len(ld)-1]-pld[len(pld)-1])
#         diffs[i+1] = ld[::-1]

#     # print([*diffs[::-1]][0])
#     # print([*[*diffs[::-1]][0]][::-1][0])
#     s += [*[*diffs[::-1]][0]][0]

# print(s)

# ---------- Clean Final ----------
f = open("sample.txt","r").read().split("\n")

def getDiff(values):return [values[1:][i] - values[:-1][i] for i in range(len(values[1:]))]

def getDiffs(values, items):return [*items, values] if all(v == 0 for v in values) else getDiffs(getDiff(values),[*items, values])

s = 0

for l in f:
    diffs = getDiffs([int(d) for d in l.split()], [])[::-1]
    for i in range(len(diffs)-1):
        ld = diffs[i+1][::-1]
        pld = diffs[i][::-1]
        ld.append(ld[len(ld)-1]-pld[len(pld)-1])
        diffs[i+1] = ld[::-1]

    s += [*[*diffs[::-1]][0]][0]

print(s)

print("-------  %s seconds -------" % (time.time() - start_time))