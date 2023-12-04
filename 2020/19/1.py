import re
import time
start_time = time.time()
x = open("sample.txt").read().strip()

rules = {}
input = x.split("\n\n")

#generate rules
for r in input[0].split("\n"):
    rule = r.split(": ")

    key = rule[0]
    value = rule[1]

    # a || b
    if re.search("a|b", value):
        rules[key] = value.replace("\"", "")
    else:
        # $ | $
        if value.find("|") > 0:
            x = []
            for ds in value.split(" | "):
                x.append(ds.split(" "))
            rules[key] = x
        # $
        else:
            values = value.split(" ")
            if len(values) > 1:
                rules[key] = values
            else:
                rules[key] = values[0]

#init rule 0
output = []
for d in rules["0"]:
    output.append(rules[d])

options = [output]
print("step 0", options)

#iterate rules and permutations
iterations = 1
looping = True
while(looping):
    exploding = True

    # if iterations == 7:
    #     break

    print("iteration", iterations)
    
    #explode and keep exploding
    while(exploding):
        explosions = 0
        newOptions = []
        didFork = False
        for o in options:
            # print("o", o)
            # resolve option and create fork
            i = 0
            for e in o:
                if type(e) is list:
                    # print("e", e)
                    didFork = True
                    # print('o', o)
                    if type(e[0]) is not list:
                        newOptions.append([*o[0:i],*e,*o[i+1:]])
                    else:
                        explosions += 1
                        newOptions.append([*o[0:i],*e[0],*o[i+1:]])
                        newOptions.append([*o[0:i],*e[1],*o[i+1:]])
                        break
                    # print("no",newOptions)
                i += 1
            if didFork == False:
                newOptions.append(o)
        
        options = newOptions
        # print(options)

        #no more explosions
        if explosions == 0:
            exploding = False
            
    print("options available", len(options))
    # print("options step 1:")
    # for i in options:
    #     print("o:",i)

    # resolve rules
    shouldStop = True
    newOptions = []
    for o in options:
        # print("o:",o)
        output = []
        for e in o:
            # print("e:",e)
            if e == "a" or e == "b":
                output.append(e)
            else:
                output.append(rules[e])
                shouldStop = False
        newOptions.append(output)
    options = newOptions

    # print("options step 2:")
    # for i in options:
    #     print("o:",i)

    if shouldStop == True:
        looping = False
    iterations += 1

# print("--------- combinations ---------")
combinations = []
for o in options:
    lo = ''
    for c in o:
        lo += c
    combinations.append(lo)
    # print(lo)

# print("end at", revolutions)
# print("out", output)
# print("opt", options)
# print("combinations", combinations)

count = 0
for c in input[1].split("\n"):
    # print(c)
    if c in combinations:
        count += 1

print (len(combinations))
print (count)
print("--- %s seconds ---" % (time.time() - start_time))