x = open("input.txt", "r")

sum = 0
games = []
i = 0
for l in x:
    i += 1
    # print("g:",i)
    g = l.strip().split(': ')
    ss = g[1].split('; ')
    r = 0 
    g = 0 
    b = 0
    for s in ss:
        sr = 0 
        sg = 0 
        sb = 0
        cs = s.split(', ')
        for c in cs:
            x = c.split(' ')
            if x[1] == "red":
                sr = int(x[0])
            if x[1] == "green":
                sg = int(x[0])
            if x[1] == "blue":
                sb = int(x[0])
        if sr > r:
            r = sr
        if sg > g:
            g = sg
        if sb > b:
            b = sb
    # print(r,g,b, r*g*b)
    sum += r*g*b

print(sum, games)