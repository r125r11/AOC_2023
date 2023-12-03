import re
import time

start_time = time.time()
f = open("input.txt","r").read().split("\n")

numbersFound = {}

def leftMostIndex(l,s):
    i = s
    while l[i-1].isdigit():
        if i-1>=0:i-=1
        else:break
    return i

def walkRight(l, s, y):
    i = s 
    key=(i,y)
    number = ''
    while l[i].isdigit():
        number += l[i]
        if i+1<len(l):i+=1
        else:break
    if number != '':
        numbersFound[key]=number

def walkLeft(l,s,y):
    i = leftMostIndex(l,s-1)  
    walkRight(l,i,y)

def walkLine(l,s,y):
    if s>0 and l[s-1].isdigit():walkLeft(l,s,y)
    if (s==0 and l[s].isdigit()) or (not l[s-1].isdigit() and l[s].isdigit()):walkRight(l,s,y)
    if not l[s].isdigit() and s<=len(l) and l[s+1].isdigit():walkRight(l,s+1,y)

def checkSurroundings(x, y):
    #up
    if y > 0:walkLine(f[y-1],x,y-1)

    #row 
    l = f[y]
    walkLine(l,x,y)

    #down
    if y < len(f):walkLine(f[y+1],x,y+1)

for i,l in enumerate(f):
    for j,e in enumerate(l):
        if re.match("[^0-9\.]",e):
            checkSurroundings(j,i)
    
# print(numbersFound)
sum = 0
for i in numbersFound:
    sum += int(numbersFound[i])
print(sum)

print("-------  %s seconds -------" % (time.time() - start_time))