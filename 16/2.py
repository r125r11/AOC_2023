import time
start_time = time.time()

f = open('input.txt','r').read().split('\n')

nodesCache = {}
for y,l in enumerate(f):
    for x,c in enumerate(l):
        match c:
            case '.': 
                nodesCache['%s,%s,%s' % (x,y,0)] = [{'x':x+1,'y':y,'d':0}]
                nodesCache['%s,%s,%s' % (x,y,1)] = [{'x':x,'y':y-1,'d':1}]
                nodesCache['%s,%s,%s' % (x,y,2)] = [{'x':x-1,'y':y,'d':2}]
                nodesCache['%s,%s,%s' % (x,y,3)] = [{'x':x,'y':y+1,'d':3}]
            case '\\':
                nodesCache['%s,%s,%s' % (x,y,0)] = [{'x':x,'y':y+1,'d':3}]
                nodesCache['%s,%s,%s' % (x,y,1)] = [{'x':x-1,'y':y,'d':2}]
                nodesCache['%s,%s,%s' % (x,y,2)] = [{'x':x,'y':y-1,'d':1}]
                nodesCache['%s,%s,%s' % (x,y,3)] = [{'x':x+1,'y':y,'d':0}]
            case '/':
                nodesCache['%s,%s,%s' % (x,y,0)] = [{'x':x,'y':y-1,'d':1}]
                nodesCache['%s,%s,%s' % (x,y,1)] = [{'x':x+1,'y':y,'d':0}]
                nodesCache['%s,%s,%s' % (x,y,2)] = [{'x':x,'y':y+1,'d':3}]
                nodesCache['%s,%s,%s' % (x,y,3)] = [{'x':x-1,'y':y,'d':2}]
            case '|':
                nodesCache['%s,%s,%s' % (x,y,0)] = [{'x':x,'y':y-1,'d':1},{'x':x,'y':y+1,'d':3}]
                nodesCache['%s,%s,%s' % (x,y,1)] = [{'x':x,'y':y-1,'d':1}]
                nodesCache['%s,%s,%s' % (x,y,2)] = [{'x':x,'y':y-1,'d':1},{'x':x,'y':y+1,'d':3}]
                nodesCache['%s,%s,%s' % (x,y,3)] = [{'x':x,'y':y+1,'d':3}]
            case '-':
                nodesCache['%s,%s,%s' % (x,y,0)] = [{'x':x+1,'y':y,'d':0}]
                nodesCache['%s,%s,%s' % (x,y,1)] = [{'x':x+1,'y':y,'d':0},{'x':x-1,'y':y,'d':2}]
                nodesCache['%s,%s,%s' % (x,y,2)] = [{'x':x-1,'y':y,'d':2}]
                nodesCache['%s,%s,%s' % (x,y,3)] = [{'x':x+1,'y':y,'d':0},{'x':x-1,'y':y,'d':2}]

pathCache = {}

startingNodes = [
    *[{'x':0,'y':y,'d':0} for y in range(len(f))],
    *[{'x':x,'y':0,'d':3} for x in range(len(f[0]))],
    *[{'x':len(f[0])-1,'y':y,'d':2} for y in range(len(f))],
    *[{'x':x,'y':len(f)-1,'d':1} for x in range(len(f[0]))],
    ]

def energise(start,i):
    visitedNodes = []
    openPaths = [start]
    values = list(start.values())
    startKey = '%s,%s,%s' % (values[0],values[1],values[2])
    startingKeys = []
    
    while len(openPaths) > 0:
        # get node
        node = openPaths.pop()
        values = list(node.values())
        nodeKey = '%s,%s,%s' % (values[0],values[1],values[2])
        
        # new chain
        if nodeKey in startingKeys:
            startKey = nodeKey
            visitedNodes = []
        
        # chain already explored
        if startKey in pathCache:
            # skip to end of path
            openPaths.append(pathCache[startKey][-1])
            continue

        # clean repeating chains
        if node not in visitedNodes:visitedNodes.append(node)
        else: continue

        # get newnodes
        nextNodes = nodesCache[nodeKey]

        # split path
        if len(nextNodes) == 2:
            # store path
            pathCache[startKey] = visitedNodes
            for n in nextNodes:
                # follow path
                if 0 <= n['x'] < len(f[0]) and 0 <= n['y'] < len(f):
                    openPaths.append(n)
                    startingKeys.append(n)
            continue
        n = nextNodes[0]
        if 0 <= n['x'] < len(f[0]) and 0 <= n['y'] < len(f):
            openPaths.append(n)
    
    fn = []
    # clean duplicated
    for n in visitedNodes:
        nn = {k:n[k] for k in n if k != 'd'}
        if nn not in fn: fn.append(nn)
    
    print('%03d-------  %s seconds -------' % ((i+1), time.time() - start_time))
    return len(fn)

print(len(startingNodes))
optimizedValues = [energise(s,i) for i,s in enumerate(startingNodes)]
print(optimizedValues)
print(max(optimizedValues))

print('-------  %s seconds -------' % (time.time() - start_time))

# import time
# start_time = time.time()

# f = open("input.txt","r").read().split("\n")

# nodesCache = {}
# for y,l in enumerate(f):
#     for x,c in enumerate(l):
#         match c:
#             case '.': 
#                 nodesCache["%s,%s,%s" % (x,y,0)] = [{'x':x+1,'y':y,'d':0}]
#                 nodesCache["%s,%s,%s" % (x,y,1)] = [{'x':x,'y':y-1,'d':1}]
#                 nodesCache["%s,%s,%s" % (x,y,2)] = [{'x':x-1,'y':y,'d':2}]
#                 nodesCache["%s,%s,%s" % (x,y,3)] = [{'x':x,'y':y+1,'d':3}]
#             case '\\':
#                 nodesCache["%s,%s,%s" % (x,y,0)] = [{'x':x,'y':y+1,'d':3}]
#                 nodesCache["%s,%s,%s" % (x,y,1)] = [{'x':x-1,'y':y,'d':2}]
#                 nodesCache["%s,%s,%s" % (x,y,2)] = [{'x':x,'y':y-1,'d':1}]
#                 nodesCache["%s,%s,%s" % (x,y,3)] = [{'x':x+1,'y':y,'d':0}]
#             case '/':
#                 nodesCache["%s,%s,%s" % (x,y,0)] = [{'x':x,'y':y-1,'d':1}]
#                 nodesCache["%s,%s,%s" % (x,y,1)] = [{'x':x+1,'y':y,'d':0}]
#                 nodesCache["%s,%s,%s" % (x,y,2)] = [{'x':x,'y':y+1,'d':3}]
#                 nodesCache["%s,%s,%s" % (x,y,3)] = [{'x':x-1,'y':y,'d':2}]
#             case '|':
#                 nodesCache["%s,%s,%s" % (x,y,0)] = [{'x':x,'y':y-1,'d':1},{'x':x,'y':y+1,'d':3}]
#                 nodesCache["%s,%s,%s" % (x,y,1)] = [{'x':x,'y':y-1,'d':1}]
#                 nodesCache["%s,%s,%s" % (x,y,2)] = [{'x':x,'y':y-1,'d':1},{'x':x,'y':y+1,'d':3}]
#                 nodesCache["%s,%s,%s" % (x,y,3)] = [{'x':x,'y':y+1,'d':3}]
#             case '-':
#                 nodesCache["%s,%s,%s" % (x,y,0)] = [{'x':x+1,'y':y,'d':0}]
#                 nodesCache["%s,%s,%s" % (x,y,1)] = [{'x':x+1,'y':y,'d':0},{'x':x-1,'y':y,'d':2}]
#                 nodesCache["%s,%s,%s" % (x,y,2)] = [{'x':x-1,'y':y,'d':2}]
#                 nodesCache["%s,%s,%s" % (x,y,3)] = [{'x':x+1,'y':y,'d':0},{'x':x-1,'y':y,'d':2}]

# startingNodes = [
#     *[{'x':0,'y':y,'d':0} for y in range(len(f))],
#     *[{'x':x,'y':0,'d':3} for x in range(len(f[0]))],
#     *[{'x':len(f[0])-1,'y':y,'d':2} for y in range(len(f))],
#     *[{'x':x,'y':len(f)-1,'d':1} for x in range(len(f[0]))],
#     ]

# def energise(start,i):
#     visitedNodes = []
#     openPaths = [start]
#     while len(openPaths) > 0:
#         # get node
#         node = openPaths.pop()
#         if node not in visitedNodes:visitedNodes.append(node)
#         else: continue

#         # get newnodes
#         values = list(node.values())
#         nextNodes = nodesCache["%s,%s,%s" % (values[0],values[1],values[2])]
#         for n in nextNodes:
#             if 0 <= n['x'] < len(f[0]) and 0 <= n['y'] < len(f):openPaths.append(n)
    
#     fn = []
#     # clean duplicated
#     for n in visitedNodes:
#         nn = {k:n[k] for k in n if k != 'd'}
#         if nn not in fn: fn.append(nn)
    
#     print("%03d-------  %s seconds -------" % ((i+1), time.time() - start_time))
#     return len(fn)

# print(len(startingNodes))
# optimizedValues = [energise(s,i) for i,s in enumerate(startingNodes)]
# print(optimizedValues)
# print(max(optimizedValues))

# print("-------  %s seconds -------" % (time.time() - start_time))