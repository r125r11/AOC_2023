x = open("./input.txt", "r")

for f in x:
    f = f.strip()
    if int(f) < 5:
        print("no")
    else:
        print(f)