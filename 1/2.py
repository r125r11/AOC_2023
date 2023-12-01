x = open("./input.txt", "r")

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# letters = list(set(''.join(digits)))

# def isDigit(word):
#     match word:
#         case "one":     return 1
#         case "two":     return 2
#         case "three":   return 3
#         case "four":    return 4
#         case "five":    return 5
#         case "six":     return 6
#         case "seven":   return 7
#         case "eight":   return 8
#         case "nine":    return 9
    
# def digit(word):
    
#     isDig = isDigit(word)
#     if isDig != None and isDig > 0:
#         return isDig
#     isDig = isDigit(word[0:3])
#     if isDig != None and isDig > 0:
#         return isDig
#     isDig = isDigit(word[1:4])
#     if isDig != None and isDig > 0:
#         return isDig
#     isDig = isDigit(word[2:5])
#     if isDig != None and isDig > 0:
#         return isDig
#     isDig = isDigit(word[0:4])
#     if isDig != None and isDig > 0:
#         return isDig
#     isDig = isDigit(word[1:5])
#     if isDig != None and isDig > 0:
#         return isDig

#     return word[0:4]

# sum = 0
# for f in x:
#     f = f.strip()

#     left = ""
#     right = ""
#     for l in f:
#         if l.isdigit():
#             left = l
#             break
#         if l not in letters:
#             left = ""
#             continue
#         left += l
#         left = str(digit(left))
#         if left.isdigit():
#             break

#     for r in f[::-1]:
#         if r.isdigit():
#             right = r
#             break
#         if r not in letters:
#             right = ""
#             continue
#         right = r + right
#         right = str(digit(right))
#         if right.isdigit():
#             break
    
#     # print("l: ", left, "| r:", right, ">>", f)
#     sum += int(left + right)

# print(sum)

sum = 0
for l in x:
    p2 = []
    for i,c in enumerate(l):
        if c.isdigit():
            p2.append(c)
        for d,val in enumerate(digits):
            if l[i:].startswith(val):
                p2.append(str(d+1))
    sum += int(p2[0]+p2[-1])
print(sum)