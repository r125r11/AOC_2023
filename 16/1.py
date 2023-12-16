import time
start_time = time.time()

f = open("sample.txt","r").read().split("\n")

visitedNodes = []
openPaths = [{'x':-1,'y':0,'d':0}]
while len(openPaths) > 0:
    # print(openPaths)
    node = openPaths.pop()
    if node not in visitedNodes:visitedNodes.append(node)
    nextNode = {k:node[k] for k in node}
    match node['d']:
        case 0: nextNode['x']+=1
        case 1: nextNode['y']-=1
        case 2: nextNode['x']-=1
        case 3: nextNode['y']+=1

    if nextNode in visitedNodes:
        continue

    # print(nextNode)
    if nextNode['x'] < 0:           continue
    if nextNode['x'] == len(f[0]):  continue
    if nextNode['y'] < 0:           continue
    if nextNode['y'] == len(f):     continue

    match f[nextNode['y']][nextNode['x']]:
        case '.': openPaths.append(nextNode)
        case '\\':
            match nextNode['d']:
                case 0: nextNode['d']=3
                case 1: nextNode['d']=2
                case 2: nextNode['d']=1
                case 3: nextNode['d']=0
            openPaths.append(nextNode)
        case '/':
            match nextNode['d']:
                case 0: nextNode['d']=1
                case 1: nextNode['d']=0
                case 2: nextNode['d']=3
                case 3: nextNode['d']=2
            openPaths.append(nextNode)
        case '|':
            match nextNode['d']:
                case 0: 
                    nextNode['d']=1
                    openPaths.append(nextNode)
                    nn = {k:nextNode[k] for k in nextNode}
                    nn['d']=3
                    openPaths.append(nn)
                case 1: openPaths.append(nextNode)
                case 2: 
                    nextNode['d']=1
                    openPaths.append(nextNode)
                    nn = {k:nextNode[k] for k in nextNode}
                    nn['d']=3
                    openPaths.append(nn)
                case 3: openPaths.append(nextNode)
        case '-':
            match nextNode['d']:
                case 0: openPaths.append(nextNode)
                case 1: 
                    nextNode['d']=0
                    openPaths.append(nextNode)
                    nn = {k:nextNode[k] for k in nextNode}
                    nn['d']=2
                    openPaths.append(nn)
                case 2: openPaths.append(nextNode)
                case 3: 
                    nextNode['d']=0
                    openPaths.append(nextNode)
                    nn = {k:nextNode[k] for k in nextNode}
                    nn['d']=2
                    openPaths.append(nn)

visitedNodes = visitedNodes[1:]

fn = []
# clean duplicated
for n in visitedNodes:
    nn = {k:n[k] for k in n if k != 'd'}
    # if nn not in fn: fn.append(nn)
    fn.append(nn)

for y,l in enumerate(f):
    nl = ''
    for x,c in enumerate(l):
        if c in ['\\','/','-','|']: nl += c
        else:
            node = {'x':x,'y':y}
            n = fn.count(node)
            if n == 0: nl += '.'
            if n > 1: nl += str(n)
            if n == 1: 
                match visitedNodes[fn.index(node)]['d']:
                    case 0: nl += '>'
                    case 1: nl += '^'
                    case 2: nl += '<'
                    case 3: nl += 'V'
    print(nl)

fn = []
# clean duplicated
for n in visitedNodes:
    nn = {k:n[k] for k in n if k != 'd'}
    if nn not in fn: fn.append(nn)

# for n in visitedNodes:
#     print(n)
print(len(fn))

print("-------  %s seconds -------" % (time.time() - start_time))