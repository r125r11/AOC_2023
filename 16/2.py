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
    # starting values
    openPaths = [start]
    values = list(start.values())
    startKey = '%s,%s,%s' % (values[0],values[1],values[2])
    pathKeyNodes = [start]

    visitedNodes = []
    
    loops = 0
    path = []
    while len(openPaths) > 0:

        loops += 1
        # get node
        node = openPaths.pop()
        values = list(node.values())
        nodeKey = '%s,%s,%s' % (values[0],values[1],values[2])

        # visited nodes
        if node not in visitedNodes: visitedNodes.append(node)
        else: continue

        # new path
        if node in pathKeyNodes:
            startKey = nodeKey
            path = []

        # path already explored
        if startKey in pathCache:
            nextNodes = pathCache[startKey]['exitNodes']
            pathKeyNodes = [*pathKeyNodes, *[n for n in nextNodes if n not in pathKeyNodes]]
            openPaths = [*openPaths, *[n for n in nextNodes if n not in openPaths]]
            continue
        
        # add note to path
        path.append(node)

        # get newnodes
        nextNodes = [n for n in nodesCache[nodeKey] if 0 <= n['x'] < len(f[0]) and 0 <= n['y'] < len(f)]

        # create 2 new paths
        if len(nextNodes) != 1:
            pathCache[startKey] = {'path':path, 'exitNodes':nextNodes}
            pathKeyNodes = [*pathKeyNodes, *[n for n in nextNodes if n not in pathKeyNodes]]
            openPaths = [*openPaths, *[n for n in nextNodes if n not in openPaths]]
            continue

        # continue on the path
        openPaths.append(nextNodes[0])

    # if i == 2 or i == 0:
    #     fn = []
    #     # clean duplicated
    #     for n in finalPath:
    #         nn = {k:n[k] for k in n if k != 'd'}
    #         # if nn not in fn: fn.append(nn)
    #         fn.append(nn)

    #     for y,l in enumerate(f):
    #         nl = ''
    #         for x,c in enumerate(l):
    #             if c in ['\\','/','-','|']: nl += c
    #             else:
    #                 node = {'x':x,'y':y}
    #                 n = fn.count(node)
    #                 if n == 0: nl += '.'
    #                 if n > 1: nl += str(n)
    #                 if n == 1: 
    #                     match finalPath[fn.index(node)]['d']:
    #                         case 0: nl += '>'
    #                         case 1: nl += '^'
    #                         case 2: nl += '<'
    #                         case 3: nl += 'v'
    #         print(nl)

    
    
    # print(len(fn))
    print('%03d-------  %s seconds -------' % ((i+1), time.time() - start_time))
    return pathKeyNodes

print(len(startingNodes))
# index = 0
# print(energise(startingNodes[index],index))
pathKeyNodes = [energise(s,i) for i,s in enumerate(startingNodes)]

pathLengths = []
for keyNodes in pathKeyNodes:
    fn = []
    for n in keyNodes:
        values = list(n.values())
        nodeKey = '%s,%s,%s' % (values[0],values[1],values[2])
        if nodeKey in pathCache:
            for nn in pathCache[nodeKey]['path']:
                nn = {k:nn[k] for k in nn if k != 'd'}
                if nn not in fn: fn.append(nn)
        else:continue

    pathLengths.append(len(fn))

print(pathLengths)
print(max(pathLengths))

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