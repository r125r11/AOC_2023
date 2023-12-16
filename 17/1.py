import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

for l in f:
    print (l)
    
print("-------  %s seconds -------" % (time.time() - start_time))