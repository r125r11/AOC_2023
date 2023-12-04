import time
start_time = time.time()

f = open("input.txt","r").read().split("\n")

print("-------  %s seconds -------" % (time.time() - start_time))