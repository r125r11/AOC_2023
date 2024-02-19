import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

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

def move_rocks(matrix):
    for i,l in enumerate(matrix):
        rpl = {-1:0}
        base = -1
        for j,c in enumerate(l):
            match c:
                case "O":
                    rpl[base] += 1
                case "#":
                    base = j
                    rpl[base] = 0
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
        matrix = [*matrix[:i],nl,*matrix[i+1:]]

    return matrix

def tumble(matrix):
    matrix = rotate_90_degree_clckwise(rotate_90_degree_clckwise(matrix))
    for _ in range(4):
        matrix = rotate_90_degree_clckwise(matrix)
        matrix = move_rocks(matrix)
    matrix = rotate_90_degree_clckwise(rotate_90_degree_clckwise(matrix))
    return matrix

t = 0
ssi = 0
rt = 1e9
# rt = 3
boards = {}
while t < rt:
    t += 1
    f = tumble(f)

    sf = ''.join(''.join(l) for l in f)
    #found sequence
    if sf in boards:
        sequenceLength = t - boards[sf]
        sequenceInRT = (rt-t)//sequenceLength
        t += sequenceInRT * sequenceLength
    boards[sf] = t

def score(G):
  ans = 0
  R = len(G)
  C = len(G[0])
  for r in range(R):
    for c in range(C):
      if G[r][c]=='O':
        ans += len(G)-r
  return ans

print(score(f))

print("-------  %s seconds -------" % (time.time() - start_time))