import time
# start_time = time.time()

# f = open("input.txt","r").read().split("\n")

# t = int(''.join(f[0].split(":")[1].split()))
# d = int(''.join(f[1].split(":")[1].split()))

# r = 0
# for i in range(t):
#     if (t-i) * i > d:
#         r +=1

# print(r)

# print("-------  %s seconds -------" % (time.time() - start_time))

start_time = time.time()

f = open("input.txt","r").read().split("\n")

t = int(''.join(f[0].split(":")[1].split()))
d = int(''.join(f[1].split(":")[1].split()))

l = 0; ul = int(t/2); ll = 0
while(True):
    if (l%2==1 and ul == l) or (l%2==0 and ul == l+1):break
    if (t-l) * l > d:   ul = l
    else:               ll = l
    l = int((ul+ll)/2)

print(t-(l*2)-1)

print("-------  %s seconds -------" % (time.time() - start_time))

start_time = time.time()

f = open("input.txt","r").read().split("\n")

t = int(''.join(f[0].split(":")[1].split()))
d = int(''.join(f[1].split(":")[1].split()))

l = 0
for i in range(int(t/2)):
    if (t-i) * i <= d:l +=1
    else: break

print(t-(l*2)+1)

print("-------  %s seconds -------" % (time.time() - start_time))