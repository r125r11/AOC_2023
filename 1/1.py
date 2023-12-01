x = open("./input.txt", "r")

sum = 0
for f in x:
    f = f.strip()

    left = 0
    right = 0
    for l in f:
        if l.isdigit():
            left = l
            break
    for r in f[::-1]:
        if r.isdigit():
            right = r
            break
    sum += int(left + right)

print(sum)