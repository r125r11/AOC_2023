import time, re
start_time = time.time()

f = open("sample.txt","r").read().split("\n")

def permutate(s,a):
    i = 0
    ai = 0
    blocks = re.findall('\.+|\?+|\#+',s)
    if '.' in blocks[-1]: blocks = blocks[:-1]
    if '.' in blocks[0]: blocks = blocks[1:]
    print(blocks)
    
    return 2
    # while i < len(s):
    #     if s[i] in ['?']:

    # tp = 0
    # p = [(s,[])]
    # while len(p) > 0:
    #     perm,fa = p.pop()


    #     #permuations
    #     i = 0
    #     while i < len(perm):
    #         if perm[i] in ['?']:
                
    #         #connected .
    #         if s[i] in ['.']:
    #             l = 1
    #             while i+l<len(s) and s[i+l] in ["."]:
    #                 l+=1
    #             #walk i
    #             i += l
    #             continue
    #         #connected #
    #         if s[i] in ['#']:
    #             l = 1
    #             while i+l<len(s) and s[i+l] in ["#"]:
    #                 l+=1
    #             #walk i
    #             i += l
    #             continue
    #         i += 1
        
    #     # add to permutations


sum = 0
for l in f:
    s,a = l.split(" ")
    a = [int(d) for d in a.split(",")]
    print(a)
    sum += permutate(s,a)

print(sum)
print("-------  %s seconds -------" % (time.time() - start_time))