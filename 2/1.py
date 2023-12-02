x = open("input.txt", "r")

sum = 0
games = []
i = 0
for l in x:
    i += 1
    g = l.strip().split(': ')
    ss = g[1].split('; ')
    valid = True
    for s in ss:
        r = 0 
        g = 0 
        b = 0
        cs = s.split(', ')
        for c in cs:
            x = c.split(' ')
            if x[1] == "red":
                r += int(x[0])
            if x[1] == "green":
                g += int(x[0])
            if x[1] == "blue":
                b += int(x[0])
        if r > 12 or g > 13 or b > 14:
            valid = False
            break
    if valid:
        games.append(i)
        sum += i

print(sum, games)